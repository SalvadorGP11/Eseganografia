Manual de Instrucciones
1. Clonar el Repositorio desde Git

Si el código está alojado en un repositorio de Git, el primer paso es clonar el repositorio.
git clone https://github.com/usuario/nombre_del_repositorio.git
cd nombre_del_repositorio

2. Crear y Activar un Entorno Virtual

Es recomendable utilizar un entorno virtual para evitar conflictos con otras instalaciones de Python y paquetes.

python3 -m venv venv
source venv/bin/activate

3. Instalar las Dependencias

Instala las dependencias necesarias. En este caso, las dependencias son Pillow y tkinter.

pip install Pillow

    Nota: tkinter generalmente viene preinstalado con Python en la mayoría de las distribuciones de Linux. Si no está instalado, puedes instalarlo usando el gestor de paquetes de tu sistema. Por ejemplo, en Debian/Ubuntu:

    sudo apt-get install python3-tk

4. Instalar steghide

Asegúrate de que steghide esté instalado en el sistema. Puedes instalarlo usando:

sudo apt-get install steghide

5. Ejecutar el Script

Para ejecutar el script, simplemente utiliza Python:

python steganography_gui.py
