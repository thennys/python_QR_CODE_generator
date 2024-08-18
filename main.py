import qrcode


class MyQR:
    def __init__(self, size, padding):
        self.qr = qrcode.QRCode(box_size=size, border=padding)


    def create_qr(self, file_name, fg, bg):
        user_input = input(f"Enter a text: ")
        # user_input = "www,mrwhyte.com"

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f"Suceesfully created!!! ({file_name})")
        except Exception as e:
            print("Error: {e}")


def main():
    myqr = MyQR(size=30,padding=2)
    myqr.create_qr('sample.png', fg='black', bg='white')

if __name__== '__main__':
    main()