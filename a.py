from pytube import YouTube
import os

link = input("Link do Vídeo: ")
yt = YouTube(link)


def principal():
    print("-----YOUTUBE DOWNLOAD-----")
    link = input("Link do Vídeo: ")
    yt = YouTube(link)

    print("\nDetalhes do Vídeo")
    # mostrar detalhes do vídeo
    # print("Título: ", yt.title)
    # print("Tempo do vídeo: ",round((yt.length//60)+(yt.length/60%1*60/100),2), " minutos")

    resolucao_alta = "1080p"
    resolucao_media = "720p"
    resolucao_baixa = "360p"
    print("Escolha a qualidade do Download:\n")
    resolucao = int(input("1 - Alta\n2 - Média\n3 - Baixa"))
    if resolucao == 1:
        ys = yt.streams.filter(res=resolucao_alta).first()
    elif resolucao == 2:
        ys = yt.streams.filter(res=resolucao_media).first()
    elif resolucao == 3:
        ys = yt.streams.filter(res=resolucao_baixa).first()

    print("DESEJA BAIXAR:")
    op = int(input("1 - Música\n2 - Bootcamp"))
    if op == 1:
        musica()
        print("Saida da funcao")
    else:
        bootcamp()
    print("FIM")

def musica():
    dir1 = 'D:\Youtube download\musicas'
    op = int(input("1 - Vídeo\n2 - Áudio"))
    if op == 1:
#Comeca o download
        print("Baixando...")
        ys.download(dir1)
        print("Download completo!")
    elif op == 2:
        ys = yt.streams.get_audio_only()
        ys.download(dir1)

def bootcamp():
    opb = {1:"Modulo1", 2:"Modulo2", 3:"Modulo3", 4:"Modulo4"}
    print("Escolha o Módulo:")
    op=int(input("Módulo 1\nMódulo 2\nMódulo 3\nMódulo 4"))
    #Comeca o download
    dir2 = f'D:\Bootcamp\{opb[op]}'
    print("Baixando...\n Pode levar alguns minutos devido a boa qualidade do Vídeo")
    ys.download(dir2)
    print("Download completo!")

principal()