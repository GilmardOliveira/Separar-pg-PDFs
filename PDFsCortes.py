import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter

def browse_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("PDF Files", "*.pdf"),))
    input_file_path.set(filename)

def split_pdf():
    input_pdf = input_file_path.get()
    output_folder = output_folder_path.get()

    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        
        for i in range(num_pages):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[i])

            output_file_path = f"{output_folder}/page_{i+1}.pdf"
            with open(output_file_path, 'wb') as output_file:
                pdf_writer.write(output_file)
                
    tk.messagebox.showinfo(title="PDF Splitter", message="PDF foi dividido com sucesso em páginas individuais!")

root = tk.Tk()
root.geometry("500x200")
root.title("PDF Splitter")

input_file_path = tk.StringVar()
output_folder_path = tk.StringVar()

label_input = tk.Label(root, text="Selecione o arquivo PDF:")
label_input.pack(pady=5)

input_frame = tk.Frame(root, width=50)
input_frame.pack(pady=5)

input_text = tk.Entry(input_frame, textvariable=input_file_path, width=40)
input_text.pack(side=tk.LEFT, padx=5)

input_button = tk.Button(input_frame, text="Selecionar", command=browse_file)
input_button.pack(side=tk.LEFT, pady=5)

label_output = tk.Label(root, text="Selecione uma pasta para salvar as páginas individuais:")
label_output.pack()

output_frame = tk.Frame(root, width=50)
output_frame.pack(pady=5)

output_text = tk.Entry(output_frame, textvariable=output_folder_path, width=40)
output_text.pack(side=tk.LEFT, padx=5)

output_button = tk.Button(output_frame, text="Selecionar", command=lambda: output_folder_path.set(filedialog.askdirectory(initialdir="/", title="Select a Folder")))
output_button.pack(side=tk.LEFT, pady=5)

enter_button = tk.Button(root, text="Enter", command=split_pdf)
enter_button.pack(pady=10)

root.mainloop()