import cv2, pytesseract, sqlite3, os, time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#cam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
cv2.namedWindow("test")
while True:
    ret, frame = cap.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if k%256 == 32:    # ESPACIO
        img_name = "DPI.JPG"
        cv2.imwrite(img_name, frame)
        break
cap.release()
cv2.destroyAllWindows()

image = cv2.imread('DPI.JPG')
imageout =image[530:558,635:700] 
text = str(((pytesseract.image_to_string(imageout,lang='spa'))))
text = text.replace('\n', ' ')
text = text.replace('', '')
print('CUI: '+ text)
#Conexion = sqlite3.connect("BBDDCovid")
#Cursor = Conexion.cursor()
#Cursor.execute("CREATE TABLE IF NOT EXISTS CIUDADANOS (CUI VARCHAR(50), Nombre VARCHAR(50), Apellido VARCHAR(50), Nacionalidad VARCHAR(50), Sexo VARCHAR(50), Edad VARCHAR(50))")
#Cursor.execute("INSERT INTO CIUDADANOS VALUES ('"+text+"', '"+text2+"', '"+text3+"', '"+text4+"', '"+text5+"', '"+text6+"')")
#Conexion.commit()
#Conexion.close()
os.remove('DPI.JPG')
cv2.imshow('Image rotated by 90 degrees',imageout)
cv2.waitKey(0) 
cv2.destroyAllWindows()