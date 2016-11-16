# coding=utf-8
#
from celery import Task
from core.common import logger,req_post
from api.models import Docker_list
from docker import Client

class BaseTask(Task):
    error_info = None
    logger = logger

    def init(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        pass
#
#
class MissionTask(BaseTask):
    docker_id=None
    def __init__(self):
        self.cli= Client(base_url='unix://var/run/docker.sock')
    def _host_config(self,instance_id,tech):
        ssh_port=10000+instance_id*2-1
        tech_port=10000+instance_id*2
        if tech=='tomcat':
            host_config=self.cli.create_host_config(port_bindings={
                        22:ssh_port,
                        8080: tech_port,
                    })
            ports=[22,8080]
            ports_detail="{0}->{1}|{2}->{3}".format(22,ssh_port,8080,tech_port)
        elif tech=='nodejs':
            host_config=self.cli.create_host_config(port_bindings={
                        22:ssh_port,
                        3000: tech_port,
                    })
            ports=[22,3000]
            ports_detail="{0}->{1}|{2}->{3}".format(22,ssh_port,3000,tech_port)
        elif tech=='php':
            host_config=self.cli.create_host_config(port_bindings={
                        22:ssh_port,
                        80: tech_port,
                    })
            ports=[22,80]
            ports_detail="{0}->{1}|{2}->{3}".format(22,ssh_port,80,tech_port)
        else:
            host_config=self.cli.create_host_config(port_bindings={
                        22:ssh_port,
                    })
            ports=[22]
            ports_detail="{0}->{1}".format(22,ssh_port)
        return ports,host_config,ports_detail
    def _start_docker(self,docker_id):
        try:
            self.cli.start(docker_id)
            return True
        except:
            return False
    def _stop_docker(self,docker_id):
        try:
            self.cli.stop(docker_id)
            return True
        except:
            return False
    def _rm_docker(self,docker_id):
        try:
            self.cli.remove_container(docker_id,force=True)
            return True
        except:
            return False
    def _create_docker(self,instance_id,tech):
        ports,host_config,ports_detail=self._host_config(instance_id,tech)
        result=self.cli.create_container('lemonbar/centos6-ssh',
                                         ports=ports,
                                         dns='',
                                         working_dir='',
                                         host_config=host_config,
                                         name='docker-shqs-{0}'.format(instance_id,))
        docker_id=result.get('Id')
        logger.debug(result)
        if self._start_docker(docker_id):
            aLL_docker=self.cli.containers(all=True)
            docker_new=[x for x in aLL_docker if x.get('Id')==docker_id][0]
            status=docker_new.get('status')
        else:
            status='unknown'
        Docker_list.objects.filter(id=instance_id).update(docker_id=docker_id,
                                                          status=status,
                                                          ports=ports_detail)
        return result

    def run(self,instance_id,command):
        docker_instance=Docker_list.objects.get(id=instance_id)
        tech=docker_instance.tech.content
        if command=='create':
            result=self._host_config(instance_id,tech)
        elif command=='start':
            result=self._start(docker_instance.docker_id)
        elif command=='stop':
            result=self._stop(docker_instance.docker_id)
        elif command=='rm':
            result=self._rm_docker(docker_instance.docker_id)
        else:
            result='not exist command'
        logger.debug(result)