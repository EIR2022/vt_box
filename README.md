# VT_BOX 
[Instrucciones](./static/Proyecto%201%20SO2.pdf)
## Integrantes 
| Nombre | Carnet |
|----------|----------|
| Israel Hurtarte    | 0900-18-1053   |
| Andrea Guerra    | 0900-18-858   |

##  Objetivo
El objetivo principal del proyecto es que el estudiante de la carrera de ingeniería en sistemas
se familiarice con los temas de virtualización muy demandados el día de hoy, conozca las
diferentes formas que pueden utilizarse en linux para poder crear hipervisores de máquinas
virtuales y pueda aplicar los conocimientos en un futuro profesional de sistemas.

## Dependencias
* Verifica si tu procesador admite la virtualización y si está habilitada. Puedes verificarlo ejecutando el siguiente comando en una terminal:
    ```bash
    egrep -c '(vmx|svm)' /proc/cpuinfo
    ```
    Si el comando devuelve un valor diferente a cero, tu procesador admite la virtualización. Si devuelve cero, tu procesador no admite la virtualización. Si el valor es diferente a cero, también verifica que la virtualización esté habilitada en la BIOS de tu equipo.
* Instala KVM, QEMU, libvirt y virsh utilizando el siguiente comando en una terminal:
    ```bash
    sudo apt-get install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
    ```
    Este comando instalará los paquetes necesarios para utilizar KVM, QEMU, libvirt y virsh.
* Una vez instalados los paquetes, asegúrate de que los servicios de libvirt estén en ejecución utilizando el siguiente comando:
    ```bash
    sudo systemctl is-active libvirtd
    ```
* Agregar el usuario a los grupos de kvm y libvirt 
    ```bash 
    sudo usermod -aG kvm $USER
    sudo usermod -aG libvirt $USER
    ```
* Utilizado para eventos de configuracion avanzada e interfaz de energia
    ```bash
    sudo apt-get install -y acpid
    ```
* Se debe de instalar la biblioteca `libvirt-python` para poder interactuar con libvirt desde Python
    ````bash
    sudo apt-get install python3-libvirt
    ````
## Adicional

* Para cargar la imagen debe de ser con extencion `.qcow2` si solo cuentas con el ISO puedes utilizar el siguiente comando para convertirlo 

    ```bash 
    qemu-img convert -f raw -O qcow2 /ruta/del/archivo.iso /ruta/destino/imagen.qcow2
    ```
*  En caso de no contar con gemu-img puedes instalarlo con la siguiente linea de comandos
    ```bash
    sudo apt-get update
    sudo apt-get install qemu-utils
    ```