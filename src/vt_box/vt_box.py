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
            <currentMemory unit='KiB'>{memory}</currentMemory>
            <vcpu placement='static'>{vcpu}</vcpu>
            <os>
                <type arch='x86_64' machine='pc-q35-4.2'>hvm</type>
                <boot dev='hd'/>
            </os>
            <features>
                <acpi/>
                <apic/>
                <vmport state='off'/>
            </features>
            <cpu mode='host-model' check='partial'/>
            <clock offset='utc'>
                <timer name='rtc' tickpolicy='catchup'/>
                <timer name='pit' tickpolicy='delay'/>
                <timer name='hpet' present='no'/>
            </clock>
            <pm>
                <suspend-to-mem enabled='no'/>
                <suspend-to-disk enabled='no'/>
            </pm>
            <devices>
                <emulator>/usr/bin/qemu-system-x86_64</emulator>
                <disk type='file' device='disk'>
                <driver name='qemu' type='qcow2'/>
                <source file='{image_path}'/>
                <target dev='vda' bus='virtio'/>
                <address type='pci' domain='0x0000' bus='0x03' slot='0x00' function='0x0'/>
                </disk>
                <disk type='file' device='cdrom'>
                <driver name='qemu' type='raw'/>
                <target dev='sda' bus='sata'/>
                <readonly/>
                <address type='drive' controller='0' bus='0' target='0' unit='0'/>
                </disk>
                <controller type='usb' index='0' model='ich9-ehci1'>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x1d' function='0x7'/>
                </controller>
                <controller type='usb' index='0' model='ich9-uhci1'>
                <master startport='0'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x1d' function='0x0' multifunction='on'/>
                </controller>
                <controller type='usb' index='0' model='ich9-uhci2'>
                <master startport='2'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x1d' function='0x1'/>
                </controller>
                <controller type='usb' index='0' model='ich9-uhci3'>
                <master startport='4'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x1d' function='0x2'/>
                </controller>
                <controller type='sata' index='0'>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x1f' function='0x2'/>
                </controller>
                <controller type='pci' index='0' model='pcie-root'/>
                <controller type='pci' index='1' model='pcie-root-port'>
                <model name='pcie-root-port'/>
                <target chassis='1' port='0x10'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0' multifunction='on'/>
                </controller>
                <controller type='pci' index='2' model='pcie-root-port'>
                <model name='pcie-root-port'/>
                <target chassis='2' port='0x11'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x1'/>
                </controller>
                <controller type='pci' index='3' model='pcie-root-port'>
                <model name='pcie-root-port'/>
                <target chassis='3' port='0x12'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x2'/>
                </controller>
                <controller type='pci' index='4' model='pcie-root-port'>
                <model name='pcie-root-port'/>
                <target chassis='4' port='0x13'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x3'/>
                </controller>
                <controller type='pci' index='5' model='pcie-root-port'>
                <model name='pcie-root-port'/>
                <target chassis='5' port='0x14'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x4'/>
                </controller>
                <controller type='pci' index='6' model='pcie-root-port'>
                <model name='pcie-root-port'/>
                <target chassis='6' port='0x15'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x5'/>
                </controller>
                <controller type='virtio-serial' index='0'>
                <address type='pci' domain='0x0000' bus='0x02' slot='0x00' function='0x0'/>
                </controller>
                <interface type='network'>
                <mac address='52:54:00:93:c2:04'/>
                <source network='default'/>
                <model type='virtio'/>
                <address type='pci' domain='0x0000' bus='0x01' slot='0x00' function='0x0'/>
                </interface>
                <serial type='pty'>
                <target type='isa-serial' port='0'>
                    <model name='isa-serial'/>
                </target>
                </serial>
                <console type='pty'>
                <target type='serial' port='0'/>
                </console>
                <channel type='unix'>
                <target type='virtio' name='org.qemu.guest_agent.0'/>
                <address type='virtio-serial' controller='0' bus='0' port='1'/>
                </channel>
                <channel type='spicevmc'>
                <target type='virtio' name='com.redhat.spice.0'/>
                <address type='virtio-serial' controller='0' bus='0' port='2'/>
                </channel>
                <input type='tablet' bus='usb'>
                <address type='usb' bus='0' port='1'/>
                </input>
                <input type='mouse' bus='ps2'/>
                <input type='keyboard' bus='ps2'/>
                <graphics type='spice' autoport='yes'>
                <listen type='address'/>
                <image compression='off'/>
                </graphics>
                <sound model='ich9'>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x1b' function='0x0'/>
                </sound>
                <video>
                <model type='qxl' ram='65536' vram='65536' vgamem='16384' heads='1' primary='yes'/>
                <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x0'/>
                </video>
                <redirdev bus='usb' type='spicevmc'>
                <address type='usb' bus='0' port='2'/>
                </redirdev>
                <redirdev bus='usb' type='spicevmc'>
                <address type='usb' bus='0' port='3'/>
                </redirdev>
                <memballoon model='virtio'>
                <address type='pci' domain='0x0000' bus='0x04' slot='0x00' function='0x0'/>
                </memballoon>
                <rng model='virtio'>
                <backend model='random'>/dev/urandom</backend>
                <address type='pci' domain='0x0000' bus='0x05' slot='0x00' function='0x0'/>
                </rng>
            </devices>
        </domain>
        '''
        domain = self.conn.defineXML(xml)
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
            domain.shutdown()
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

    def list_domains(self):
        domains = self.conn.listAllDomains()
        vms = []
        for domain in domains:
            vms.append(domain.name())
        return vms
    
    def get_vm_state(self,name):
        vm = self.conn.lookupByName(name)
        state, _ = vm.state()
        return state

    def __del__(self):
        self.conn.close()