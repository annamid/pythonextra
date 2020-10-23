from PIL import Image, ImageDraw, ImageFont

afbeelding = Image.open("katje.jpg")

lettertype = ImageFont.truetype("impact.ttf", 32)

tekengebied = ImageDraw.Draw(afbeelding)

tekst = "girls wanting attention"
tekst_x = 200
tekst_y = 50
tekengebied.multiline_text((tekst_x, tekst_y), tekst,
                           font=lettertype, fill=(0, 0, 0))
tekengebied.multiline_text((tekst_x-2, tekst_y-2),
                           tekst, font=lettertype, fill=(255, 255, 255))
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print("tekstbreedte=" + str(tekst_breedte) +
      ", tekst_hoogte=" + str(tekst_hoogte))

afbeelding.show()

afbeelding.save("meme_met_tekst.png")