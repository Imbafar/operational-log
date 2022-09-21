from io import BytesIO

from xhtml2pdf import pisa
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import Record


def download(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    texts = record.texts.all()
    template = loader.get_template("to_pdf/my_template.html")
    length = f"rowspan={len(texts)}"
    context = {
        "record": record,
        "texts": texts,
        "font": settings.FONT_DIR,
        "length": length,
    }

    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type="application/pdf")
        response["Content-Disposition"] = 'filename="home_page.pdf"'
        return response
    return
