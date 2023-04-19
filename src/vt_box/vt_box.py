import os
import subprocess
import libvirt
class VmManager:
    def __init__(self):
        self.conn = libvirt.open('qemu:///system')
        if self.conn == None:
            raise Exception('Failed to open connection to QEMU.')

    def create_vm(self, name, memory, vcpu, image_path):
        # Define la configuración de la máquina virtual
        xml = f'''
            <domain type='kvm'>
                <name>{name}</name>
                <memory unit='KiB'>{memory}</memory>
                <vcpu placement='static'>{vcpu}</vcpu>
                <os>
                    <type arch='x86_64' machine='pc-i440fx-2.9'>hvm</type>
                    <boot dev='hd'/>
                </os>
                <devices>
                    <disk type='file' device='disk'>
                        <driver name='qemu' type='qcow2'/>
                        <source file='{image_path}'/>
                        <target dev='vda' bus='virtio'/>
                    </disk>
                    <interface type='network'>
                        <source network='default'/>
                        <model type='virtio'/>
                    </interface>
                    <graphics type='spice' port='5900' autoport='yes'>
                        <listen type='none'/>
                        <image compression='off'/>
                    </graphics>
                    <video>
                        <model type='virtio' heads='1' primary='yes'/>
                    </video>
                </devices>
            </domain>
        '''
        domain = self.conn.createXML(xml, flags=0)
        if domain == None:
            raise Exception('Error al crear la maquina virtual')
        return domain

    def start_vm(self, name):
        domain = self.conn.lookupByName(name)
        if domain == None:
            raise Exception('No existe una maquina virtual con ese nombre')
        if domain.create() < 0:
            raise Exception('No se inicio correctamente la maquina virtual')
        return domain

    def stop_vm(self, name):
        try: 
            domain = self.conn.lookupByName(name)
            if domain == None:
                raise Exception('No existe una maquina virtual con ese nombre')
            domain.destroy()
            return True
        except:
            raise Exception('No se detuvo correctamente la maquina virtual')        

    def get_vms_active(self):
        vms = []
        for vm_id in self.conn.listDomainsID():
            vm = self.conn.lookupByID(vm_id)
            if vm.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
                vms.append({
                    'name': vm.name(),
                    'status': vm.state(),
                    'id': vm_id
                })
        return vms
    
    def get_vm_info(self, name):
        vm = self.conn.lookupByName(name)
        info = {}
        info['name'] = name
        info['state'] = vm.state()[0]
        info['max_mem'] = vm.maxMemory()
        info['num_vcpus'] = vm.maxVcpus()
        info['uuid'] = vm.UUIDString()
        print (info)
        return info
    
    def connect_to_vm(self, name):
        vm_id = self.conn.lookupByName(name).ID()
        cmd = ['virt-viewer', str(vm_id), '--attach']
        subprocess.Popen(cmd)

    def __del__(self):
        self.conn.close()