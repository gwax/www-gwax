<!DOCTYPE html>
<%
    rows = [[v for v in range(0,10)] for row in range(0,10)]
%><html>
<head>
  <title>Base template</title>
</head>

<body>
  <h1>Hello world!</h1>
  <h2>data = ${data}</h2>

  <table>
      % for row in rows:
          ${makerow(row)}
      % endfor
  </table>

  <%def name="makerow(row)">
      <tr>
      % for name in row:
          <td>${name}</td>\
      % endfor
      </tr>
  </%def>
</body>
</html>
