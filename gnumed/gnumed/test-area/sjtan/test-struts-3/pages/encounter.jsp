
<%@page contentType="text/html"%>
<%@page pageEncoding="UTF-8"%>
<%@taglib uri="http://jakarta.apache.org/struts/tags-html" prefix="html"%>
<%@taglib uri="http://jakarta.apache.org/struts/tags-bean" prefix="bean"%>
<%@taglib uri="http://jakarta.apache.org/struts/tags-logic" prefix="logic"%>
<%@taglib uri="http://jakarta.apache.org/struts/tags-nested" prefix="nested"%>

<%--  See vaccination regarding indexed properties for <logic:iterate>
 1. need a indexed getter method on the bean.  2. the id attribute of logic:iterate must
be the name of the property targetted by the getter
e.g. getNarrative(index) ...  id='narrative'
--%>
<html>
<head>
    <title>Encounter </title>

    <script language='JavaScript' type='text/javascript' >
    <!--
    function getRelativeURL(hashUrl) {
       return "<%=request.getContextPath()+"//ClinicalEdit.do?id="+((org.gnumed.testweb1.data.DemographicDetail)request.getAttribute("detail")).getId() %>" + hashUrl;
    }
    
    function testCheckBox(sel) {
        document.getElementById(sel).style.display="none";
    }
    function show(divName) {
    
    document.getElementById(divName).style.setAttribute("display", "block");
         
       
    return true;
            
    }
    
    function hide(divName) {
    if ( document.getElementById ) {
    
    var div = document.getElementById(divName);
    if (div ) {
    div.style.visibility="hidden";
    return true;
    }
            
    
    }
    //-->
    </script>

</head>
<body>
<h3> <bean:message key="encounter.entry.title"/> </h3>
    <%-- <jsp:useBean id="beanInstanceName" scope="session" class="beanPackage.BeanClassName" /> --%>
    <%-- <jsp:getProperty name="beanInstanceName"  property="propertyName" /> --%>
    <html:base/>
    <div class="errors">
        <html:errors/>
        
    </div>
    
    
    
    <jsp:include page="./patient_detail_block.jsp"/>
    
    
    <div id="testdiv" class="testdiv0" style='visibility:hidden;'>
    <h2>THis should be hidden </h2>
    </div>
    <%--
    <html:form action="/SaveClinical">
--%>
        <table>
            
           
            <tr>
            <td>
                <bean:message key="current.encounter"/>
            </td>
            
            <td>
                <bean:message key="encounter.time"/>
                <bean:write name="clinicalUpdateForm" property="encounter.started"/>
            </td>
            <td>
                <bean:message key="encounter.location"/>
                <html:select  name="clinicalUpdateForm" property="encounter.location" >
                    <html:option value="1">consulting room </html:option>
                    <html:option value="2">nursing home </html:option>
                </html:select>
            </td>
             
            </tr>
            
        </table>
         
        <logic:iterate id="narrative" name="clinicalUpdateForm" 
        property="encounter.narratives"   
         scope="request" indexId="index">
            <a name='linkNarrative<%=index%>' </a>
            <table>
                <tr>
                
                <td>
                    <bean:message key="health.issue"/>
                </td>
                <td> <input type="checkbox" name="newHealthIssue<%=index%>" value=''
                onchange="if (this.checked) 
                            { 
                                document.getElementById('sel<%=index%>').style.display='none';
                                document.getElementById('txtNewHealthIssue<%=index%>').style.display='block';
                            } else {
                                document.getElementById('sel<%=index%>').style.display='block'; 
                                document.getElementById('txtNewHealthIssue<%=index%>').style.display='none';
                            }
                            return true;"
                 value='1' title='create health issue'/></td>               
                <td>
                <div id="sel<%=index%>">
                
                    <nested:select name="clinicalNarrative" property="healthIssueName" indexed="true" value="0"
                        onchange=""
                        >
                        <html:option value="0">not selected</html:option>
                        <html:option value="1">xxxDEFAULTxxx</html:option>
                        <html:option value="2">asthma</html:option>
                    </nested:select>
                
                
                </div>
                
                <div id="txtNewHealthIssue<%=index%>" style="display:none" >
                    
                                New Health Issue:
                                <html:text name="narrative" property="healthIssueName" indexed="true"/>
                        
                
                </div>
                
                </td>
                   
                <td>
                    <!--
                    <a href="#e<%=index%>" onclick="var prefix='clinNarrative'; show(prefix, <%=index%>); return false;"
                    >Show episode</a>
                    <a href="#e<%=index%>" onclick="var prefix='clinNarrative'; hide(prefix, <%=index%>); return false;"
                    >Hide</a>
                    -->
                    <a href="javascript:getRelativeURL('#linkNarrative<%=index%>')"
                    onclick="document.getElementById('clinNarrative<%=index%>').style.display='block'; return true;" > show </a> 
                   
                    <a href="javascript:getRelativeURL('#linkNarrative<%=index%>')"
                    onclick="document.getElementById('clinNarrative<%=index%>').style.display='none'; return true;" > hide </a> 
                </td>
                    
                </tr>    
                
            </table>
                
            <div id='clinNarrative<%=index%>' style='display:<%=(String)((index.intValue() == 0)? "block":"none")%>'  >   
              
                <table> 
                    
                    <tr>
                        <td>
                            <bean:message key="episode.notes" />
                        </td>
                    </tr>
                    <tr>
                    <td COLSPAN='2'>
                        <html:textarea  name="narrative" property="narrative"  rows="6" cols="40" indexed="true" />
                    
                    </td>
                    </tr>
                </table>
            </div>
                    
            
        </logic:iterate>
        <%--
        <table>
            <td>
                <html:submit altKey="change.clinical" ><bean:message key="change.clinical"/></html:submit>
            </td>
            <td>
                <html:reset altKey="reset" />
            </td>
            </tr>
        </table>

    </html:form>
--%>

<html:javascript formName="clinicalUpdateForm"
   dynamicJavascript="true" staticJavascript="false"/> 


</body>
</html>
