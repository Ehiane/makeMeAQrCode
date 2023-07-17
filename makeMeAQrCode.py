import qrcode

def main():
    user_link = input("Enter your link here:");
    code_name = input("Enter name of the qrcode: ")
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4,
    )
    qr.add_data(user_link);
    qr.make(fit=True);
    image = qr.make_image(fill_color = "black", back_color = "white");
    image.save(f"{code_name}.png");



main();
