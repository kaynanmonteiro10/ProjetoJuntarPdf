import comtypes.client
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PyPDF2 import PdfMerger
from datetime import datetime
from PIL import Image, ImageTk

historico = []

def selecionar_arquivos():
    arquivos = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    return list(arquivos)

def juntar_pdfs():
    pdf_list = selecionar_arquivos()
    if pdf_list:
        nome_arquivo = simpledialog.askstring("Nome do Arquivo", "Digite o nome do arquivo final:")
        if nome_arquivo:
            if not nome_arquivo.endswith('.pdf'):
                nome_arquivo += '.pdf'
            merger = PdfMerger()
            for pdf in pdf_list:
                merger.append(pdf)
            merger.write(nome_arquivo)
            merger.close()
            messagebox.showinfo("Sucesso", f"Parabéns, você juntou os PDFs como {nome_arquivo}!")
            historico.append(nome_arquivo)
            atualizar_historico()

def atualizar_historico():
    texto_historico.config(state=tk.NORMAL)
    texto_historico.delete(1.0, tk.END)
    texto_historico.insert(tk.END, "Histórico de PDFs Juntados:\n")
    for item in historico:
        texto_historico.insert(tk.END, f"- {item}\n")
    texto_historico.config(state=tk.DISABLED)

def mostrar_tela_principal():
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg="#000000")
    frame = tk.Frame(root, bg="#000000")
    frame.pack(expand=True, fill=tk.BOTH)
    data_atual = datetime.now().strftime("%d/%m/%Y")
    data_label = tk.Label(frame, text=f"Data de Hoje: {data_atual}", bg="#000000", fg="#ff0000", font=("Helvetica", 12))
    data_label.pack(pady=10)
    btn_juntar = tk.Button(
        frame, text="Selecionar e Juntar PDFs", command=juntar_pdfs, bg="#ff0000", fg="white",
        font=("Helvetica", 14, "bold"), relief=tk.RAISED, bd=5, highlightthickness=0, padx=10, pady=10, cursor="hand2"
    )
    btn_juntar.pack(pady=20)
    global texto_historico
    texto_historico = tk.Text(frame, height=10, bg="#000000", fg="#ff0000", font=("Helvetica", 12))
    texto_historico.pack(pady=20, padx=10, fill=tk.BOTH)
    atualizar_historico()

root = tk.Tk()
root.title("Juntar PDFs")
root.geometry("800x600")
root.iconbitmap(r"C:\Users\Relatorios\Downloads\images_Nfk_1.ico")
tela_apresentacao = tk.Frame(root, bg="#000000")
tela_apresentacao.pack(expand=True, fill=tk.BOTH)
mensagem_inicial = tk.Label(tela_apresentacao, text="Seja Bem-Vindo Kaynan!", bg="#000000", fg="#ff0000", font=("Helvetica", 14, "bold"))
mensagem_inicial.pack(pady=20)
mensagem_subtitulo = tk.Label(tela_apresentacao, text="Vamos Juntar Vários PDFs Hoje?", bg="#000000", fg="#ff0000", font=("Helvetica", 12))
mensagem_subtitulo.pack(pady=10)
caminho_imagem = r"C:\Users\Relatorios\Downloads\pngwing.com.png"
try:
    imagem_dragao = Image.open(caminho_imagem)
    imagem_dragao = imagem_dragao.resize((800, 450), Image.Resampling.LANCZOS)
    imagem_dragao_tk = ImageTk.PhotoImage(imagem_dragao)
    label_imagem_dragao = tk.Label(tela_apresentacao, image=imagem_dragao_tk, bg="#000000")
    label_imagem_dragao.pack(pady=10)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
btn_iniciar = tk.Button(
    tela_apresentacao, text="Iniciar", command=mostrar_tela_principal, bg="#ff0000", fg="white",
    font=("Helvetica", 14, "bold"), relief=tk.RAISED, bd=5, highlightthickness=0, padx=10, pady=10, cursor="hand2"
)
btn_iniciar.pack(pady=20)
root.mainloop()
