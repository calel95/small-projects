import os
import time
from pytube import YouTube

print("-----YOUTUBE DOWNLOAD-----")
#diretorio pode ser alterado conforme a necessidade, atentar para as barras
dir1 = 'D:\Youtube download\musicas'

link = input("Link do Vídeo: ")
yt = YouTube(link)

print("\nDetalhes do Vídeo")
print("Título: ", yt.title)
print("Tempo do vídeo: ", round((yt.length // 60) + (yt.length / 60 % 1 * 60 / 100), 2), " minutos")

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

op = int(input("1 - Vídeo\n2 - Áudio\n"))
if op == 1:
    print("Baixando...")
    ys.download(dir1)
elif op == 2:
    ys = yt.streams.get_audio_only()
    ys.download(dir1)
    print("Download completo!")
else:
    print("OPÇÃO INVÁLIDA, PROGRAMA FECHANDO...")
    time.sleep(3)