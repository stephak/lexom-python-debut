from fpdf import FPDF
import f214_getlog as getlog
import datetime


today=datetime.datetime.now().strftime("%Y%m%d") #pour avoir un string obtenu à partir de la date du jour

class PDF(FPDF):    
    def header(self):         #parametrage du header
        # Logo
        self.image('alteca_logo.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(10, 10, 'Requetes lentes du Squid ('+today +')', 0, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer           #parametrage du footer
    def footer(self):
        # Position a 1.5 cm du bas
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 8)
#for i in range(1, 41):
#    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)



tab=getlog.get_weird_queries("/Users/stephanehakni/PycharmProjects/dev","squidAnonymise.db",10)
i=0
for line in tab :
    if i%2==0:
        pdf.set_text_color(0, 0, 255)
    else:
        pdf.set_text_color(0, 0, 0)
    #pdf.cell(5,str(line))
    pdf.multi_cell(0, 10, str(line), 1, 1)
    i+=1



filename='squidReport_'+today+".pdf"
pdf.output(filename, 'F')