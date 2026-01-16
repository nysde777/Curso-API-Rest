from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.get("/user-xml")
def get_user_xml():
    xml_content = """
    <user>
        <id>19</id>
        <name>Maria Juana</name>
        <active>true</active>
    </user>
    """
    return Response(
        content=xml_content,
        media_type="application/xml"
    )