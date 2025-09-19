from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>geetha</title>

    </head>
    <body>
        <h1 align="center">Device specification=25018001</h1>
        <table border="6" cellspacing="7" cellpadding="3">
            
            <tr bgcolor="pink">
                <td>S.No</td>
                <td>Device specification</td>
                <td>Description</td>
            </tr>
            <tr bgcolor="yellow">
                <td>1</td>
                <td>storage</td>
                <td>238</td>
            </tr>
            <tr bgcolor="yellow">
                <td>2</td>
                <td>graphics card</td>
                <td>128MB</td>
            </tr>
            <tr bgcolor="yellow">
                <td>3</td>
                <td>installed ram</td>
                <td>4.00GB</td>
            </tr>
            <tr bgcolor="yellow">
                <td>4</td>
                <td>Device name</td>
                <td>LAPTOP-A5CUFGGB</td>
            </tr>
            <tr bgcolor="yellow">
                <td>5</td>
                <td>Device id</td>
                <td>0059CDF0-63C7-436E-BA49-5838E518CAD8</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever() 