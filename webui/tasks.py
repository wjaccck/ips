#coding=utf-8
from celery import Task as T
from core.common import logger,ANSRunner,Send_message
from api.models import Machine,Ipv4Address
import redis

class BaseTask(T):
    error_info = None
    logger = logger

    def init(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        pass

class MissionTask(BaseTask):

    def _get_ipv4(self,name):
        ipv4,ipv4_status=Ipv4Address.objects.get_or_create(name=name)
        return ipv4

    def run(self):
        host_list=[x.console_ip.name for x in Machine.objects.all()]
        resource = [{"hostname": x, "username": "root", "ssh_key": "/root/.ssh/id_rsa"} for x in host_list]
        rbt = ANSRunner(resource)
        rbt.run_model(host_list=host_list, module_name='setup',module_args="")
        data = rbt.get_model_result()
        result = rbt.handle_cmdb_data(data)
        wrong_list=[x.get('console_ip') for x in result if x.get('status')==3]
        done_list=[x for x in result if x.get('status')==0]
        failed_list=[x.get('console_ip') for x in result if x.get('status')==1]
        unreachable_list=[x.get('console_ip') for x in result if x.get('status')==2]
        for m in done_list:
            console_ip=m.get('console_ip')
            console_host=Machine.objects.get(console_ip=self._get_ipv4(name=console_ip))
            console_host.cpu=m.get('cpu')
            console_host.kernel=m.get('kernel')
            console_host.cpu_number=m.get('cpu_number')
            console_host.vcpu_number=m.get('vcpu_number')
            console_host.cpu_core=m.get('cpu_core')
            console_host.hostname=m.get('hostname')
            console_host.memory=m.get('memory')
            console_host.disk=m.get('disk_total')
            console_host.swap=m.get('swap')
            console_host.product=m.get('product')
            console_host.selinux=m.get('selinux')
            console_host.distribution=m.get('distribution')
            console_host.distribution_version=m.get('distribution_version')
            console_host.manufacturer=m.get('manufacturer')
            console_host.serial=m.get('serial')
            console_host.status=m.get('status')
            console_host.idc='hzbj'
            console_host.company='shihui'
            for n in m.get('ipv4'):
                console_host.ipv4.add(self._get_ipv4(n))
            console_host.save()

        send_msg=''
        if wrong_list:
            send_msg=send_msg+'\r\n wrong_list:\r\n{0}'.format('\r\n'.join(wrong_list))
        if failed_list:
            send_msg = send_msg + '\r\n failed_list:\r\n{0}'.format('\r\n'.join(failed_list))
        if wrong_list:
            send_msg = send_msg + '\r\n unreachable_list info:\r\n{0}'.format('\r\n'.join(unreachable_list))

        if send_msg:
            logger.info(send_msg)
            Send_message().run(send_msg)
