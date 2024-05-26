import os
import subprocess
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

#A
def detect_and_remove_steganography(image_path, output_path, cleaned_image_path, passphrase, text_widget):
    try:
        subprocess.run(['steghide', 'extract', '-sf', image_path, '-xf', output_path, '-p', passphrase], check=True)
        with open(output_path, 'r') as file:
            extracted_message = file.read()
        text_widget.delete("1.0", END)
        text_widget.insert(END, extracted_message)
        messagebox.showinfo("Éxito", f"Contenido oculto extraído y guardado en: {output_path}")
        with Image.open(image_path) as img:
            img.save(cleaned_image_path)
        messagebox.showinfo("Éxito", f"Imagen limpia guardada en: {cleaned_image_path}")
    except subprocess.CalledProcessError:
        text_widget.delete("1.0", END)
        text_widget.insert(END, "No se detectó contenido oculto.")
        messagebox.showerror("Error", f"No se detectó contenido oculto en: {image_path}")
#B
def clean_image(image_path, cleaned_image_path, text_widget):
    try:
        with Image.open(image_path) as img:
            img.save(cleaned_image_path)
        text_widget.delete("1.0", END)
        text_widget.insert(END, "La imagen ha sido limpiada correctamente.")
        messagebox.showinfo("Éxito", f"Imagen limpia guardada en: {cleaned_image_path}")
    except Exception as e:
        text_widget.delete("1.0", END)
        text_widget.insert(END, f"Error al procesar la imagen: {e}")
        messagebox.showerror("Error", f"Error al procesar la imagen: {e}")
#C
def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, END)
    entry.insert(0, filename)
#D
def create_extract_and_clean_window():
    window = Toplevel(root)
    window.title("Extraer y Limpiar con Frase de Paso")

    # Ruta de la imagen
    Label(window, text="Ruta de la imagen:").grid(row=0, column=0, padx=10, pady=10)
    image_entry = Entry(window, width=50)
    image_entry.grid(row=0, column=1, padx=10, pady=10)
    Button(window, text="Buscar", command=lambda: browse_file(image_entry)).grid(row=0, column=2, padx=10, pady=10)

    # Ruta del archivo de salida
    Label(window, text="Ruta del archivo de salida:").grid(row=1, column=0, padx=10, pady=10)
    output_entry = Entry(window, width=50)
    output_entry.grid(row=1, column=1, padx=10, pady=10)
    Button(window, text="Buscar", command=lambda: browse_file(output_entry)).grid(row=1, column=2, padx=10, pady=10)

    # Ruta para guardar la imagen limpia
    Label(window, text="Ruta para guardar la imagen limpia:").grid(row=2, column=0, padx=10, pady=10)
    cleaned_image_entry = Entry(window, width=50)
    cleaned_image_entry.grid(row=2, column=1, padx=10, pady=10)
    Button(window, text="Buscar", command=lambda: browse_file(cleaned_image_entry)).grid(row=2, column=2, padx=10, pady=10)

    # Frase de paso
    Label(window, text="Frase de paso:").grid(row=3, column=0, padx=10, pady=10)
    passphrase_entry = Entry(window, show="*", width=50)
    passphrase_entry.grid(row=3, column=1, padx=10, pady=10)

    # Texto extraído
    Label(window, text="Mensaje extraído:").grid(row=4, column=0, padx=10, pady=10)
    text_widget = Text(window, height=10, width=50)
    text_widget.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    # Botones
    Button(window, text="Extraer y limpiar", command=lambda: detect_and_remove_steganography(image_entry.get(), output_entry.get(), cleaned_image_entry.get(), passphrase_entry.get(), text_widget)).grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    Button(window, text="Cerrar", command=window.destroy).grid(row=6, column=0, columnspan=3, padx=10, pady=10)
#E
def create_clean_only_window():
    window = Toplevel(root)
    window.title("Limpiar sin Usar la Frase de Paso")

    # Ruta de la imagen
    Label(window, text="Ruta de la imagen:").grid(row=0, column=0, padx=10, pady=10)
    image_entry = Entry(window, width=50)
    image_entry.grid(row=0, column=1, padx=10, pady=10)
    Button(window, text="Buscar", command=lambda: browse_file(image_entry)).grid(row=0, column=2, padx=10, pady=10)

    # Ruta para guardar la imagen limpia
    Label(window, text="Ruta para guardar la imagen limpia:").grid(row=1, column=0, padx=10, pady=10)
    cleaned_image_entry = Entry(window, width=50)
    cleaned_image_entry.grid(row=1, column=1, padx=10, pady=10)
    Button(window, text="Buscar", command=lambda: browse_file(cleaned_image_entry)).grid(row=1, column=2, padx=10, pady=10)

    # Texto extraído
    Label(window, text="Mensaje:").grid(row=2, column=0, padx=10, pady=10)
    text_widget = Text(window, height=10, width=50)
    text_widget.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    # Botones
    Button(window, text="Limpiar", command=lambda: clean_image(image_entry.get(), cleaned_image_entry.get(), text_widget)).grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    Button(window, text="Cerrar", command=window.destroy).grid(row=4, column=0, columnspan=3, padx=10, pady=10)
#F
def main():
    global root
    root = Tk()
    root.title("Sistema de Esteganografía")

    # Menú principal
    Label(root, text="Seleccione una opción:").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    Button(root, text="Extraer y Limpiar con Frase de Paso", command=create_extract_and_clean_window).grid(row=1, column=0, padx=10, pady=10)
    Button(root, text="Limpiar sin Usar la Frase de Paso", command=create_clean_only_window).grid(row=1, column=1, padx=10, pady=10)
    Button(root, text="Salir", command=root.quit).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()
#G
if __name__ == "__main__":
    main()

