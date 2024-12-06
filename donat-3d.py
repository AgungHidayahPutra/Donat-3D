from vpython import *
import random

# Membuat canvas interaktif
scene = canvas(
    title="3D Donut",
    width=1000,
    height=800,
    background=color.black
)

# Membuat torus/donat
donat = ring(
    pos=vector(0, 0, 0),  # Posisi pusat donat
    axis=vector(0, 0, 1),  # Arah sumbu utama donat
    radius=3,  # Radius besar donat
    thickness=1,  # Ketebalan donat
    color=vector(0.8, 0.6, 0.4),  # Warna donat (gradasi cokelat muda)
    shininess=0.6  # Efek kilap
)

# Menambahkan efek pencahayaan
light1 = local_light(pos=vector(5, 5, 5), color=color.white)  # Sumber cahaya pertama
light2 = local_light(pos=vector(-5, -5, -5), color=color.yellow)  # Sumber cahaya kedua

# Animasi rotasi
while True:
    rate(60)  # Frame per detik
    donat.rotate(
        angle=0.02,  # Sudut rotasi dalam radian
        axis=vector(0, 1, 0),  # Rotasi pada sumbu Y
        origin=vector(0, 0, 0)  # Titik pusat rotasi
    )
