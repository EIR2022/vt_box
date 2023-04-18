from pyvbox import VirtualBoxManager,NetworkAttachmentType

# Crea una instancia de VirtualBoxManager
vbox = VirtualBoxManager()

# Crea una nueva máquina virtual con las opciones deseadas
vm_options = {
    'name': 'MiVM',
    'ostype': 'Linux26_64',
    'cpus': 2,
    'memory': 2048,
    'hard_drive': {'size': 10 * 1024 * 1024 * 1024, 'filename': 'MiVM.vdi'}
}
vm = vbox.create_vm(vm_options)

# Configura el adaptador de red de la máquina virtual
network_adapter = vm.get_network_adapter(0)
network_adapter.enabled = True
network_adapter.attachment_type = NetworkAttachmentType.bridged

# Inicia la máquina virtual en modo gráfico
vm.launch(['--type', 'gui'])