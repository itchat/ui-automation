import ddddocr


class Cap:

    ocr = ddddocr.DdddOcr(show_ad=False)

    def recognition(self, path):
        code = self.ocr.classification(open(path, "rb").read())
        return code

