<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h1>schema.rb</h1>
  <xsl:for-each select="database/table">
	<h3><xsl:value-of select="@name"/></h3>
    <table border="1">
      <xsl:for-each select="field">
        <tr>
          <td><xsl:value-of select="@name"/></td>
        </tr>
      </xsl:for-each>
    </table>
  </xsl:for-each>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>