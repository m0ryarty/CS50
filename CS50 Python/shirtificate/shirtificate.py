from fpdf import FPDF


def main():
    name = input('Name: ')

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 45)
    pdf.text(40, 30, "CS50 Shirtificate")
    pdf.image("shirtificate.png", x=1, y=60)
    pdf.set_font("helvetica", "B", 25)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.text(50, 140, f'{name} took CS50')
    pdf.output("shirtificate.pdf")


main()
