from odoo import models
import base64
import io



class ParkirCardXlsx(models.AbstractModel):
    _name = 'report.parkir.report_parkir_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, parkirs):
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})
        format_2 = workbook.add_format({'align': 'center', 'bold': True})


        for obj in parkirs:
            report_name = obj.parkir_nomor
            # One sheet by parkirs
            sheet = workbook.add_worksheet(report_name)
            row = 3
            col = 3
            sheet.set_column('D:D', 12)
            sheet.set_column('E:E', 13)

            row += 1
            sheet.merge_range(row, col, row, col + 2, 'PARKIR BESMENT', format_1)

            row += 1
            if obj.image:
                parkir_image = io.BytesIO(base64.b64decode(obj.image))
                sheet.insert_image(row, col, "image.png", {'image_data': parkir_image, 'x_scale': 0000.2, 'y_scale' : 000.1})
            row += 6

            row += 1
            sheet.write(row, col, '1', format_2)
            sheet.write(row, col + 1, 'Parkir Record')
            sheet.write(row, col + 2, obj.name_seq, format_2)

            row += 1
            sheet.write(row, col, '2', format_2)
            sheet.write(row, col + 1, 'Plat Nomor')
            sheet.write(row, col + 2, obj.parkir_nomor, format_2)

            row += 1
            sheet.write(row, col, '3', format_2)
            sheet.write(row, col + 1, 'Kendaraan Roda')
            sheet.write(row, col + 2, obj.parkiran_roda, format_2)

            row += 1
            sheet.write(row, col, '4', format_2)
            sheet.write(row, col + 1, 'Nominal Parkir')
            sheet.write(row, col + 2, obj.parkir_nominal, format_2)

            row += 2
            sheet.merge_range(row, col, row +1, col + 2, '', format_1)





            # bold = workbook.add_format({'bold': True})

            # row += 6
            # sheet.write(row, col, 'Plat Nomor', bold)
            # sheet.write(row, col + 1, obj.parkir_nomor, bold)