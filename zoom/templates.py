"""
    templates.zoom
"""

from zoom.page import page


def app_not_found(request):
    # pylint: disable=unused-argument
    return """
    <h1>System Message</h1>
    <p>This site is currently under construction.</p>
    """


page_not_found = """
    <div class="jumbotron">
        <h1>Page Not Found</h1>
        <p>The page you requested could not be found.
        Please contact the administrator or try again.<p>
    </div>
    """

site_not_found = """
    <head>
    <style>
    body {{
      margin: 0;
      padding: 0;
      font: 20px 'RobotoRegular', Arial, sans-serif;
      font-weight: 100;
      height: 100%;
      color: #0f1419;
    }}
    h1 {{
      padding-top: 0.75em;
      text-align: center;
      font-size: 3.5em;
      margin-bottom: 0.25em;
    }}
    div.info {{
      display: table;
      background: #e8eaec;
      padding: 20px 20px 20px 20px;
      border: 1px dashed black;
      border-radius: 10px;
      margin: 0px auto auto auto;
      font: 20px Courier;
    }}
    div.info p {{
        display: table-row;
        margin: 5px auto auto auto;
    }}
    div.info p span {{
        display: table-cell;
        padding: 10px;
    }}
    div.smaller p span {{
        color: #3D5266;
    }}
    h1, h2 {{
      font-weight: 100;
    }}
    #footer {{
        position: fixed;
        bottom: 36px;
        width: 100%;
        font-size: 0.8em;
    }}
    #center {{
        width: 400px;
        margin: 0 auto;
        font: 12px Courier;
    }}
    </style>
    </head>
    <body>
    <h1>ZOOM</h1>
    <div class="info">
        <p><span>Host ............:</span> <span>{request.host}</span></p>
        <p><span>Server&nbsp;name .....:</span> <span>{node}</span></p>
        <p><span>Protocol ........:</span> <span>{request.protocol}</span></p>
        <p><span>URI .............:</span> <span>{request.path}</span></p>
        <p><span>Date ............:</span> <span>{date}</span></p>
        <p><span>Client&nbsp;IP .......:</span> <span>{request.ip_address}</span></p>
        <p><span>Module ..........:</span> <span>{request.module}</span></p>
    </div>
    <div id="footer">
        <div id="center" align="center">
            <img src="https://www.dynamic-solutions.com/themes/dsi2014/images/dynamicsolutions.png">
            Request ID: {request.request_id}<br/>
            &copy; <a href="https://www.dynamic-solutions.com">Dynamic Solutions Inc.</a> 2016
        </div>
    </div>
    </body>
    """
