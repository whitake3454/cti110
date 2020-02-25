<!DOCTYPE HTML >
<html  lang="en-US">
 <head>
  <title>Review Submission History: P2T1- Sales Prediction &ndash; ...</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta id="request-method" name="request-method" content="GET">
  <meta name="author" content="Blackboard">
  <meta name="copyright" content="&copy; 1997-2020 Blackboard Inc. All Rights Reserved. U.S. Patent No. 7,493,396 and 7,558,853. Additional Patents Pending.">
  <meta name="keywords" content="Blackboard">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="-1">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    
<script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={licenseKey:"232bf20b67",applicationID:"63650369"};window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var i=n[t]={exports:{}};e[t][0].call(i.exports,function(n){var i=e[t][1][n];return r(i||n)},i,i.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<t.length;i++)r(t[i]);return r}({1:[function(e,n,t){function r(){}function i(e,n,t){return function(){return o(e,[u.now()].concat(f(arguments)),n?null:this,t),n?void 0:this}}var o=e("handle"),a=e(4),f=e(5),c=e("ee").get("tracer"),u=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",d=l+"ixn-";a(p,function(e,n){s[n]=i(l+n,!0,"api")}),s.addPageAction=i(l+"addPageAction",!0),s.setCurrentRouteName=i(l+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,i="function"==typeof n;return o(d+"tracer",[u.now(),e,t],r),function(){if(c.emit((i?"":"no-")+"fn-start",[u.now(),r,i],t),i)try{return n.apply(this,arguments)}catch(e){throw c.emit("fn-err",[arguments,this,e],t),e}finally{c.emit("fn-end",[u.now()],t)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=i(d+n)}),newrelic.noticeError=function(e,n){"string"==typeof e&&(e=new Error(e)),o("err",[e,u.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){var t=e.getEntries();t.forEach(function(e){"first-paint"===e.name?c("timing",["fp",Math.floor(e.startTime)]):"first-contentful-paint"===e.name&&c("timing",["fcp",Math.floor(e.startTime)])})}function i(e,n){var t=e.getEntries();t.length>0&&c("lcp",[t[t.length-1]])}function o(e){if(e instanceof s&&!l){var n,t=Math.round(e.timeStamp);n=t>1e12?Date.now()-t:u.now()-t,l=!0,c("timing",["fi",t,{type:e.type,fid:n}])}}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var a,f,c=e("handle"),u=e("loader"),s=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){a=new PerformanceObserver(r),f=new PerformanceObserver(i);try{a.observe({entryTypes:["paint"]}),f.observe({entryTypes:["largest-contentful-paint"]})}catch(p){}}if("addEventListener"in document){var l=!1,d=["click","keydown","mousedown","pointerdown","touchstart"];d.forEach(function(e){document.addEventListener(e,o,!1)})}}},{}],3:[function(e,n,t){function r(e,n){if(!i)return!1;if(e!==i)return!1;if(!n)return!0;if(!o)return!1;for(var t=o.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var f=navigator.userAgent,c=f.match(a);c&&f.indexOf("Chrome")===-1&&f.indexOf("Chromium")===-1&&(i="Safari",o=c[1])}n.exports={agent:i,version:o,match:r}},{}],4:[function(e,n,t){function r(e,n){var t=[],r="",o=0;for(r in e)i.call(e,r)&&(t[o]=n(r,e[r]),o+=1);return t}var i=Object.prototype.hasOwnProperty;n.exports=r},{}],5:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,i=t-n||0,o=Array(i<0?0:i);++r<i;)o[r]=e[n+r];return o}n.exports=r},{}],6:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function i(e){function n(e){return e&&e instanceof r?e:e?c(e,f,o):o()}function t(t,r,i,o){if(!l.aborted||o){e&&e(t,r,i);for(var a=n(i),f=v(t),c=f.length,u=0;u<c;u++)f[u].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function d(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return p[e]=p[e]||i(t)}function w(e,n){u(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var h={},y={},b={on:d,addEventListener:d,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:w,abort:a,aborted:!1};return b}function o(){return new r}function a(){(s.api||s.feature)&&(l.aborted=!0,s=l.backlog={})}var f="nr@context",c=e("gos"),u=e(4),s={},p={},l=n.exports=i();l.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(i.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return e[n]=r,r}var i=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){i.buffer([e],r),i.emit(e,n,t)}var i=e("ee").get("handle");n.exports=r,r.ee=i},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,o,function(){return i++})}var i=1,o="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!x++){var e=E.info=NREUM.info,n=d.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();u(y,function(n,t){e[n]||(e[n]=t)}),c("mark",["onload",a()+E.offset],null,"api");var t=d.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function i(){"complete"===d.readyState&&o()}function o(){c("mark",["domContent",a()+E.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(f=Math.max((new Date).getTime(),f))-E.offset}var f=(new Date).getTime(),c=e("handle"),u=e(4),s=e("ee"),p=e(3),l=window,d=l.document,m="addEventListener",v="attachEvent",g=l.XMLHttpRequest,w=g&&g.prototype;NREUM.o={ST:setTimeout,SI:l.setImmediate,CT:clearTimeout,XHR:g,REQ:l.Request,EV:l.Event,PR:l.Promise,MO:l.MutationObserver};var h=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1167.min.js"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),E=n.exports={offset:f,now:a,origin:h,features:{},xhrWrappable:b,userAgent:p};e(1),e(2),d[m]?(d[m]("DOMContentLoaded",o,!1),l[m]("load",r,!1)):(d[v]("onreadystatechange",i),l[v]("onload",r)),c("mark",["firstbyte",f],null,"api");var x=0,O=e(6)},{}],"wrap-function":[function(e,n,t){function r(e){return!(e&&e instanceof Function&&e.apply&&!e[a])}var i=e("ee"),o=e(5),a="nr@original",f=Object.prototype.hasOwnProperty,c=!1;n.exports=function(e,n){function t(e,n,t,i){function nrWrapper(){var r,a,f,c;try{a=this,r=o(arguments),f="function"==typeof t?t(r,a):t||{}}catch(u){l([u,"",[r,a,i],f])}s(n+"start",[r,a,i],f);try{return c=e.apply(a,r)}catch(p){throw s(n+"err",[r,a,p],f),p}finally{s(n+"end",[r,a,c],f)}}return r(e)?e:(n||(n=""),nrWrapper[a]=e,p(e,nrWrapper),nrWrapper)}function u(e,n,i,o){i||(i="");var a,f,c,u="-"===i.charAt(0);for(c=0;c<n.length;c++)f=n[c],a=e[f],r(a)||(e[f]=t(a,u?f+i:i,o,f))}function s(t,r,i){if(!c||n){var o=c;c=!0;try{e.emit(t,r,i,n)}catch(a){l([a,t,r,i])}c=o}}function p(e,n){if(Object.defineProperty&&Object.keys)try{var t=Object.keys(e);return t.forEach(function(t){Object.defineProperty(n,t,{get:function(){return e[t]},set:function(n){return e[t]=n,n}})}),n}catch(r){l([r])}for(var i in e)f.call(e,i)&&(n[i]=e[i]);return n}function l(n){try{e.emit("internal-error",n)}catch(t){}}return e||(e=i),t.inPlace=u,t.flag=a,t}},{}]},{},["loader"]);</script>
  <link rel="SHORTCUT ICON" type="image/x-icon" href="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/ui/bb-icon2.ico">
     <link rel="stylesheet" type="text/css" href="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/common/shared.css?v=3800.0.0-rel.30+071ab51" id="css_0">
     <link rel="stylesheet" type="text/css" href="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/themes/as_2012/theme.css?v=3800.0.0-rel.30+071ab51" id="css_1">
     <link rel="stylesheet" type="text/css" href="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/themes/as_2012/app_nav.css?v=3800.0.0-rel.30+071ab51" id="css_2">
     <link rel="stylesheet" type="text/css" href="/branding/_1_1/brand.css?ts=1507797631756&v=3800.0.0-rel.30+071ab51" id="css_3">
     <link rel="stylesheet" type="text/css" href="/webapps/assignment/css/assignment.css?v=3800.0.0-rel.30+071ab51" id="css_4">
     <link rel="stylesheet" type="text/css" href="/webapps/rubric/css/rubrics.css?v=3800.0.0-rel.30+071ab51" id="css_5">
     <link rel="stylesheet" type="text/css" href="/webapps/inline-grading/css/grading.css?v=3800.0.0-rel.30+071ab51" id="css_6">
     <link rel="stylesheet" type="text/css" href="/webapps/cloud-profiles/css/opt_in_lightbox.css?b2=3800.0.0-rel.30+071ab51&v=3800.0.0-rel.30+071ab51" id="css_7">
     <link rel="stylesheet" type="text/css" href="/webapps/videointegration/css/video-integration.css?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51" id="css_8">
     <link rel="stylesheet" type="text/css" href="/webapps/allyintegration/css/ally-integration.css?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51" id="css_9">
          <style type="text/css" id="courseMenuCustomCSS">


.noteditmode .listCm .courseMenu a:hover span, 
.noteditmode .listCm .courseMenu a:focus span {
	color:#FFFFCC!important;
}

#courseMenuPalette_paletteTitleHeading h3 {
   background-color: #444444;
}

#courseMenu_folderView ul {
   background-color: #444444;
}

#courseMenuPalette div.navPaletteContent ul li a,
#courseMenuPalette h3 a,
#previewCourseMenu h3 a,
.navPaletteContent h3 a.submenuLink:before,
.navPaletteContent h3 a.submenuLink_active:before,
#courseMenuPalette div.navPaletteContent ul li a span,
#courseMenuPalette .navPaletteContent .subhead
{
  color: #FFFFCC;
  text-shadow: none;
  /*should only be 2012*/
}

#courseMenuPalette ul.courseMenu li.divider hr
{
  background-color: #FFFFCC;
}

#courseMenuPalette ul.courseMenu li h4
{
  color: #FFFFCC;
}

#courseMenuPalette h4.treehead
{
  color: #FFFFCC;
}

#courseMenuPalette div.navPaletteContent
{
  background-color: #444444;
}

#courseMenuPalette_contents li {
  background-color: #444444;
}

/*Active course menu view bubble stem*/
#courseMenuPalette .actionBarMicro .active > a:after {
  border-bottom-color: #444444;
}

/* 2016 Theme override default blue and white on course creation */



/* if theme is classic */

</style>
      <style type="text/css">.topGlobalLinks a.home{background-image:url(https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/console/icons/home_0.gif)}.bottom-buttons-home a{background-image:url(https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/console/icons/home_0.gif);background-repeat:no-repeat;background-position:50% 0}.topGlobalLinks a.help{background-image:url(https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images-ltr/console/icons/help_0.gif)}.bottom-buttons-help a{background-image:url(https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images-ltr/console/icons/help_0.gif);background-repeat:no-repeat;background-position:50% 0}.topGlobalLinks a.logout{background-image:url(https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/console/icons/logout_0.gif)}.global-nav-bar .logout-link,.global-nav-bar .logout-link:hover,.global-nav-bar .logout-link:focus{background-image:url(https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/console/icons/logout_0.gif);background-repeat:no-repeat;background-position:50% 0}</style>
       <link rel="stylesheet" type="text/css" media="print" href="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/ui/styles/print.css?v=3800.0.0-rel.30+071ab51">
    <script type="text/javascript" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/javascript/i18n.js?v=3800.0.0-rel.30+071ab51"></script>
      <script language='javascript' type='text/javascript'>

var JS_RESOURCES = new Object();

function _init_bundle_JS_RESOURCES() {

    JS_RESOURCES['validation.email'] = 'A fully qualified email address (for example, info@blackboard.com) must be entered.';
    JS_RESOURCES['validation.radio.required'] = 'Make a selection to continue.';
    JS_RESOURCES['assessment.incomplete.confirm.backtrackProhibited.survey'] = 'The following questions may be incomplete:\n {0}\nClick cancel to return to the survey. Click Ok to save the incomplete answer.';
    JS_RESOURCES['common.list.separator.comma'] = '{0}, {1}';
    JS_RESOURCES['active.filter.search.terms'] = 'Search Terms';
    JS_RESOURCES['validation.points.decimal.places.error.location'] = 'Point Values are limited to 5 decimal places: {0}.';
    JS_RESOURCES['validation.maximum_length.plural'] = 'Must not contain more than {1} characters: {0}.\nReduce the size of the input by {2} characters.';
    JS_RESOURCES['assessment.incomplete.confirm.backtrackProhibited'] = 'The following questions may be incomplete:\n {0}\nClick cancel to return to the test. Click Ok to save the incomplete answer.';
    JS_RESOURCES['validation.multiSelect.minItems'] = 'Multiselect box should contain at least {0} number of items.';
    JS_RESOURCES['validation.cmp_field.required'] = 'A value must be provided for {0}\nwhen {1} field is not empty';
    JS_RESOURCES['warning.email'] = 'Email address is a recommended field. Users will be unable to use parts of the system without an email address.';
    JS_RESOURCES['validation.maximum_length.no_name.singular'] = 'Must not contain more than {0} characters.\nReduce the size of the input by one character.';
    JS_RESOURCES['validation.multiSelect.maxItems'] = 'Multiselect box should not contain more than {0} number of items.';
    JS_RESOURCES['validation.number'] = 'A valid numeric value must be entered: {0}.';
    JS_RESOURCES['validation.date.required'] = 'A complete date value must be provided: {0}.';
    JS_RESOURCES['portalmodule.section.remove'] = 'Delete: {0}?';
    JS_RESOURCES['show.helptext'] = 'Show Help Text';
    JS_RESOURCES['validation.password'] = 'Password cannot be empty or contain only spaces.';
    JS_RESOURCES['validation.percent'] = 'A valid percent value between 0 and 100 must be entered.';
    JS_RESOURCES['validation.mismatch'] = 'The values entered do not match: {0}.\nConfirm: {0}.';
    JS_RESOURCES['validation.maximum_length.no_name.plural'] = 'Must not contain more than {0} characters.\nReduce the size of the input by {1} characters.';
    JS_RESOURCES['validation.invalid_value'] = 'Invalid numeric value provided: {0}.';
    JS_RESOURCES['field_name.substitute'] = '\'\'{0}\'\' input field';
    JS_RESOURCES['validation.required'] = 'A value must be provided: {0}.';
    JS_RESOURCES['active.filter.free.form.text.blank'] = 'Specify a value for the search text field';
    JS_RESOURCES['validate.alignment.missing.content'] = 'You selected alignments but did not select any alignable content to copy.';
    JS_RESOURCES['validation.system_role.reserve'] = '"bb" is not permitted at the beginning of a role ID.';
    JS_RESOURCES['validation.date_past'] = 'The end date cannot be earlier than the start date.';
    JS_RESOURCES['validation.invalid_chars'] = 'Contains illegal characters: {0}.\nDelete these characters: {1}';
    JS_RESOURCES['confirm.delete_item_value'] = 'This item {0} will be deleted. Continue?';
    JS_RESOURCES['hide.helptext'] = 'Hide Help Text';
    JS_RESOURCES['validate.range.lessthen.str'] = 'Less Than {0}';
    JS_RESOURCES['validation.date_past.confirm'] = 'The time is in the past.\nContinue with this time?';
    JS_RESOURCES['validate.login.invalid.username.or.pass'] = 'Enter a username and password.';
    JS_RESOURCES['validation.negative'] = 'A valid non-negative value must be entered: {0}.';
    JS_RESOURCES['validation.url'] = 'A valid URL (for example, http://www.myschool.edu) must be entered.';
    JS_RESOURCES['validate.range.overlap'] = 'criteria ({0}) overlaps criteria ({1}).';
    JS_RESOURCES['validate.range.between.str'] = 'Between {0} and {1}';
    JS_RESOURCES['validation.portal.tool.items.remove'] = 'Delete: {0}?';
    JS_RESOURCES['validation.association.refresh.confirm'] = 'The associated items information might have been updated.\nClick \'OK\' to refresh the list or click \'Cancel\' to keep the current page.';
    JS_RESOURCES['validate.enrolloptions.error.codeconflict'] = 'The Access Code Enrollment option conflicts with the selection of {instructor} Led enrollment.';
    JS_RESOURCES['validation.points.decimal.places'] = 'Point Values are limited to 5 decimal places.';
    JS_RESOURCES['validation.option.required'] = 'At least one option must be selected from the list.';
    JS_RESOURCES['list.checkToSelectAllItems'] = 'Check to select all items';
    JS_RESOURCES['active.filter.changed.alert'] = 'criteria now contains';
    JS_RESOURCES['vtbe.artifact.footer.validate.nameIfSaveArtifact'] = 'Specify a Name in order to Save as a Reusable Object.';
    JS_RESOURCES['validate.invalidate.number'] = 'Please input valid number instead of {0}.';
    JS_RESOURCES['validation.valid_course_id'] = 'Course id contains illegal characters or multibyte characters.';
    JS_RESOURCES['assessment.incomplete.confirm'] = 'The following questions may be incomplete:\n {0}\nClick cancel to return to the test. Click Ok to submit assessment.';
    JS_RESOURCES['validate.enrolloptions.error.nooption'] = 'Warning: Choose either the {instructor} Led or the Self-Enrollment option.';
    JS_RESOURCES['validation.date_equal'] = 'The start date cannot be equal to the end date.';
    JS_RESOURCES['validation.cmp_field.rejected'] = 'The {0} cannot be used without a corresponding {1} value.';
    JS_RESOURCES['validation.time.required'] = 'A complete time value must be provided: {0}.';
    JS_RESOURCES['validation.integer_number'] = 'A valid integer numeric value must be entered: {0}.';
    JS_RESOURCES['validation.maximum_length'] = 'Must not contain more than 255 characters';
    JS_RESOURCES['validate.enrolloptions.error.emailrequestconflict'] = 'The selected email enrollment option conflicts with the self-enrollment selection.';
    JS_RESOURCES['invalid_char.space'] = 'space';
    JS_RESOURCES['validate.range.morethen.str'] = 'More Than {0}';
    JS_RESOURCES['notification.submit'] = 'Action already submitted.\nWait until the action is complete.';
    JS_RESOURCES['validation.plain_text.confirm'] = 'To display equations correctly in this document, Smart Text or HTML format must be selected.\nClick \'OK\' to save in selected Plain Text format or click \'Cancel\' to select a new format.';
    JS_RESOURCES['invalid_char.comma'] = 'comma';
    JS_RESOURCES['validation.allow_negtive.percent'] = 'A valid percent value between -100 and 100 must be entered.';
    JS_RESOURCES['confirm.remove_item'] = 'This action is final and cannot be undone. Continue?';
    JS_RESOURCES['list.uncheckToDeselectAllItems'] = 'Uncheck to deselect all items';
    JS_RESOURCES['validation.maximum_length.singular'] = 'Must not contain more than {1} characters: {0}.\nReduce the size of the input by one character.';
    JS_RESOURCES['validation.rubric.decimalplaces'] = 'Too many decimal places. Maximum is 5.';
    JS_RESOURCES['validation.minimum_length'] = 'A minimum of {0} characters must be entered: {1}.';
    JS_RESOURCES['vtbe.artifact.footer.validate.saveLocationIfSaveArtifact'] = 'Specify a location for the Reusable Object.';
    JS_RESOURCES['assessment.incomplete.confirm.survey'] = 'The following questions may be incomplete:\n {0}\nClick cancel to return to the survey. Click Ok to submit assessment.';
    JS_RESOURCES['validation.image_type'] = 'Unknown image type: {0}. Image may not display correctly.';
    JS_RESOURCES['validate.invalidate.number.space'] = 'Space';

    JS_RESOURCES.getString = i18n_get_string;
    JS_RESOURCES.getFormattedString = i18n_get_formatted_string;

}

_init_bundle_JS_RESOURCES();

</script>
<script language='javascript' type='text/javascript'>

var LOCALE_SETTINGS = new Object();

function _init_bundle_LOCALE_SETTINGS() {

    LOCALE_SETTINGS['LOCALE_SETTINGS.ADDRESS_FIELD_ORDER'] = 'STREET_1 STREET_2 CITY STATE ZIP_CODE COUNTRY';
    LOCALE_SETTINGS['number_format.exponent'] = 'eE';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NAME.COLUMN.2'] = '{1}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.YEAR_CHARACTER.03255'] = '';
    LOCALE_SETTINGS['BBI18N.SOLARIS_CHARSET'] = 'ISO8859-1';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NAME.COLUMN.1'] = '{0}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_COLUMN_FORMAT_MONTH.03255'] = 'ddd';
    LOCALE_SETTINGS['LOCALE_SETTINGS.internal_date_format'] = 'MM/dd/yy';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_TITLE_FORMAT_MONTH.03259'] = 'MMMM yyyy';
    LOCALE_SETTINGS['LOCALE_SETTINGS.TIME_ORDER.00519'] = 'HMP';
    LOCALE_SETTINGS['float.format'] = '^(([0-9]{1,3}(\\,[0-9]{3})*)|[0-9]*)(\\.[0-9]+)?$';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NAME.SORT_COLUMN'] = 'familyName';
    LOCALE_SETTINGS['LOCALE_SETTINGS.SHORT'] = '{1} {3}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAY_SHORT.02097'] = 'SUN MON TUE WED THU FRI SAT';
    LOCALE_SETTINGS['float.allow.negative.format'] = '^((([-]?[0-9]{1,3}(\\,[0-9]{3})*)|[-]?[0-9]*)(\\.[0-9]+)?|\\.[0-9]+)?$';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_TYPE'] = 'GREGORIAN';
    LOCALE_SETTINGS['LOCALE_SETTINGS.GIVEN_INITIAL_FAMILY_NAME'] = '{4} {3}';
    LOCALE_SETTINGS['efloat.format'] = '^[+-]?[0-9]*(\\.[0-9]+)?([eE][+-]?[0-9]+)?$';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_TITLE_FORMAT_WEEK.03260'] = 'MMM d[ yyyy]{ \'&#8212;\'[ MMM] d yyyy}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_FULL.02100'] = 'January February March April May June July August September October November December';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NUMBERS_HIJRI_LOCALIZED.00521'] = 'NO';
    LOCALE_SETTINGS['LOCALE_SETTINGS.LONG'] = '{0} {1} {2} {3}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.WORK_FIELD_ORDER'] = 'JOB_TITLE DEPARTMENT COMPANY B_PHONE_1 B_PHONE_2 B_FAX';
    LOCALE_SETTINGS['LOCALE_SETTINGS.REPORT_FONT_NAME.03169'] = 'ARIAL.TTF';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_FULL_HIJRI.02100'] = 'Muḥarram,Ṣafar,Rabīʿ\'al-Awwal,Rabīʿ\'ath-Thānī,Jumādā\'al-Ūlā,Jumādā\'ath-Thāniya,Rajab,Shaʿbān,Ramaḍān,Shawwāl,Dhū\'al-Qaʿda,Dhū\'al-Ḥijja';
    LOCALE_SETTINGS['LOCALE_SETTINGS.GREETING'] = 'Welcome, {1}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_SHORT.00520'] = 'Jan Feb  Mar Apr  May Jun Jul Aug Sep Oct Nov Dec';
    LOCALE_SETTINGS['LOCALE_SETTINGS.REPORT_FONT_SIZE.03168'] = '8';
    LOCALE_SETTINGS['number_format.thousands_sep'] = ',';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_COLUMN_FORMAT_WEEK.03256'] = 'ddd M/d';
    LOCALE_SETTINGS['LOCALE_SETTINGS.SHORT_SURNAME'] = '{3}, {1}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.AM_PM.00522'] = 'AM PM';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DATE_ORDER.00519'] = 'MDY';
    LOCALE_SETTINGS['LOCALE_SETTINGS.PHONE_FIELD_ORDER'] = 'H_PHONE_1 H_PHONE_2 H_FAX M_PHONE';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAY_MIN.02099'] = 'Su Mo Tu We Th Fr Sa';
    LOCALE_SETTINGS['LOCALE_SETTINGS.24HR_SUPPORT.03208'] = '0';
    LOCALE_SETTINGS['LOCALE_SETTINGS.REPORT_FONT_PATH.03170'] = 'C:/WINNT/Fonts';
    LOCALE_SETTINGS['LOCALE_SETTINGS.FIRST_DAY_OF_WEEK.03207'] = '0';
    LOCALE_SETTINGS['BBI18N.WINDOWS_CHARSET'] = 'ISO-8859-1';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_SHORT_HIJRI.00520'] = 'Muḥarram,Ṣafar,Rabīʿ\'I,Rabīʿ\'II,Jumādā\'I,Jumādā\'II,Rajab,Shaʿbān,Ramaḍān,Shawwāl,Dhū\'al-Qaʿda,Dhū\'al-Ḥijja';
    LOCALE_SETTINGS['BBI18N.LINUX_CHARSET'] = 'iso88591';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAY_CHARACTER.03253'] = '';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_CHARACTER.03254'] = '';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NAME.COLUMN_ORDER'] = 'title,givenName,middleName,familyName,suffix,otherName';
    LOCALE_SETTINGS['number_format.decimal_point'] = '.';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_TITLE_FORMAT_DAY.03258'] = 'dddd, MMM d, yyyy';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAYS.00521'] = '01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAY_FULL.02098'] = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday';
    LOCALE_SETTINGS['LOCALE_SETTINGS.date_display_pattern'] = 'MM/DD/YY';
    LOCALE_SETTINGS['LOCALE_SETTINGS.EXTENDED_SURNAME'] = '{3}';
    LOCALE_SETTINGS['thousand.sep.format'] = ',';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NUMBERS_HIJRI.00521'] = '0 1 2 3 4 5 6 7 8 9';
    LOCALE_SETTINGS['LOCALE_SETTINGS.ADDRESS_ORDER.07832'] = 'street,city,region,postal_code,country';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_COLUMN_FORMAT_DAY.03257'] = 'dddd M/d';

    LOCALE_SETTINGS.getString = i18n_get_string;
    LOCALE_SETTINGS.getFormattedString = i18n_get_formatted_string;

}

_init_bundle_LOCALE_SETTINGS();

</script>

      <script language='javascript' type='text/javascript'>

var LOCALE_SETTINGS = new Object();

function _init_bundle_LOCALE_SETTINGS() {

    LOCALE_SETTINGS['LOCALE_SETTINGS.ADDRESS_FIELD_ORDER'] = 'STREET_1 STREET_2 CITY STATE ZIP_CODE COUNTRY';
    LOCALE_SETTINGS['number_format.exponent'] = 'eE';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NAME.COLUMN.2'] = '{1}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.YEAR_CHARACTER.03255'] = '';
    LOCALE_SETTINGS['BBI18N.SOLARIS_CHARSET'] = 'ISO8859-1';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NAME.COLUMN.1'] = '{0}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_COLUMN_FORMAT_MONTH.03255'] = 'ddd';
    LOCALE_SETTINGS['LOCALE_SETTINGS.internal_date_format'] = 'MM/dd/yy';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_TITLE_FORMAT_MONTH.03259'] = 'MMMM yyyy';
    LOCALE_SETTINGS['LOCALE_SETTINGS.TIME_ORDER.00519'] = 'HMP';
    LOCALE_SETTINGS['float.format'] = '^(([0-9]{1,3}(\\,[0-9]{3})*)|[0-9]*)(\\.[0-9]+)?$';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NAME.SORT_COLUMN'] = 'familyName';
    LOCALE_SETTINGS['LOCALE_SETTINGS.SHORT'] = '{1} {3}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAY_SHORT.02097'] = 'SUN MON TUE WED THU FRI SAT';
    LOCALE_SETTINGS['float.allow.negative.format'] = '^((([-]?[0-9]{1,3}(\\,[0-9]{3})*)|[-]?[0-9]*)(\\.[0-9]+)?|\\.[0-9]+)?$';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_TYPE'] = 'GREGORIAN';
    LOCALE_SETTINGS['LOCALE_SETTINGS.GIVEN_INITIAL_FAMILY_NAME'] = '{4} {3}';
    LOCALE_SETTINGS['efloat.format'] = '^[+-]?[0-9]*(\\.[0-9]+)?([eE][+-]?[0-9]+)?$';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_TITLE_FORMAT_WEEK.03260'] = 'MMM d[ yyyy]{ \'&#8212;\'[ MMM] d yyyy}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_FULL.02100'] = 'January February March April May June July August September October November December';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NUMBERS_HIJRI_LOCALIZED.00521'] = 'NO';
    LOCALE_SETTINGS['LOCALE_SETTINGS.LONG'] = '{0} {1} {2} {3}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.WORK_FIELD_ORDER'] = 'JOB_TITLE DEPARTMENT COMPANY B_PHONE_1 B_PHONE_2 B_FAX';
    LOCALE_SETTINGS['LOCALE_SETTINGS.REPORT_FONT_NAME.03169'] = 'ARIAL.TTF';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_FULL_HIJRI.02100'] = 'Muḥarram,Ṣafar,Rabīʿ\'al-Awwal,Rabīʿ\'ath-Thānī,Jumādā\'al-Ūlā,Jumādā\'ath-Thāniya,Rajab,Shaʿbān,Ramaḍān,Shawwāl,Dhū\'al-Qaʿda,Dhū\'al-Ḥijja';
    LOCALE_SETTINGS['LOCALE_SETTINGS.GREETING'] = 'Welcome, {1}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_SHORT.00520'] = 'Jan Feb  Mar Apr  May Jun Jul Aug Sep Oct Nov Dec';
    LOCALE_SETTINGS['LOCALE_SETTINGS.REPORT_FONT_SIZE.03168'] = '8';
    LOCALE_SETTINGS['number_format.thousands_sep'] = ',';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_COLUMN_FORMAT_WEEK.03256'] = 'ddd M/d';
    LOCALE_SETTINGS['LOCALE_SETTINGS.SHORT_SURNAME'] = '{3}, {1}';
    LOCALE_SETTINGS['LOCALE_SETTINGS.AM_PM.00522'] = 'AM PM';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DATE_ORDER.00519'] = 'MDY';
    LOCALE_SETTINGS['LOCALE_SETTINGS.PHONE_FIELD_ORDER'] = 'H_PHONE_1 H_PHONE_2 H_FAX M_PHONE';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAY_MIN.02099'] = 'Su Mo Tu We Th Fr Sa';
    LOCALE_SETTINGS['LOCALE_SETTINGS.24HR_SUPPORT.03208'] = '0';
    LOCALE_SETTINGS['LOCALE_SETTINGS.REPORT_FONT_PATH.03170'] = 'C:/WINNT/Fonts';
    LOCALE_SETTINGS['LOCALE_SETTINGS.FIRST_DAY_OF_WEEK.03207'] = '0';
    LOCALE_SETTINGS['BBI18N.WINDOWS_CHARSET'] = 'ISO-8859-1';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_SHORT_HIJRI.00520'] = 'Muḥarram,Ṣafar,Rabīʿ\'I,Rabīʿ\'II,Jumādā\'I,Jumādā\'II,Rajab,Shaʿbān,Ramaḍān,Shawwāl,Dhū\'al-Qaʿda,Dhū\'al-Ḥijja';
    LOCALE_SETTINGS['BBI18N.LINUX_CHARSET'] = 'iso88591';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAY_CHARACTER.03253'] = '';
    LOCALE_SETTINGS['LOCALE_SETTINGS.MONTH_CHARACTER.03254'] = '';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NAME.COLUMN_ORDER'] = 'title,givenName,middleName,familyName,suffix,otherName';
    LOCALE_SETTINGS['number_format.decimal_point'] = '.';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_TITLE_FORMAT_DAY.03258'] = 'dddd, MMM d, yyyy';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAYS.00521'] = '01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31';
    LOCALE_SETTINGS['LOCALE_SETTINGS.DAY_FULL.02098'] = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday';
    LOCALE_SETTINGS['LOCALE_SETTINGS.date_display_pattern'] = 'MM/DD/YY';
    LOCALE_SETTINGS['LOCALE_SETTINGS.EXTENDED_SURNAME'] = '{3}';
    LOCALE_SETTINGS['thousand.sep.format'] = ',';
    LOCALE_SETTINGS['LOCALE_SETTINGS.NUMBERS_HIJRI.00521'] = '0 1 2 3 4 5 6 7 8 9';
    LOCALE_SETTINGS['LOCALE_SETTINGS.ADDRESS_ORDER.07832'] = 'street,city,region,postal_code,country';
    LOCALE_SETTINGS['LOCALE_SETTINGS.CALENDAR_COLUMN_FORMAT_DAY.03257'] = 'dddd M/d';

    LOCALE_SETTINGS.getString = i18n_get_string;
    LOCALE_SETTINGS.getFormattedString = i18n_get_formatted_string;

}

_init_bundle_LOCALE_SETTINGS();

</script>

         <script type="text/javascript" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/javascript/cdn.js"></script>
    <script type="text/javascript" src="/groupjs/4258AF0D5B3FE65B6ADDE926F6A60273.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/assignment/dwr_open/interface/UserDataDWRFacade.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/blackboard/dwr_open/interface/MashupDWRFacade.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/assignment/js/grade_assignment.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/assignment/dwr_open/interface/MashupDWRFacade.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/rubric/js/rubricGradingService.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/javascript/titlebartagutils.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/inline-grading/js/aggregate-grading.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/gradebook/js/gradebook_utils.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/inline-grading/js/attempt-grading.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/inline-grading/js/inline-grading-list.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/inline-grading/js/comment-box.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/vtbe-tinymce/javascript/vtbeTinyMce.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/portfolio/js/portfolio.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/inline-grading/js/common.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/inline-grading/js/inline-grading.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/assignment/dwr_open/interface/CourseMenuDWRFacade.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/assignment/dwr_open/interface/UserPageInstructionsSettingDWRFacade.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/javascript/dwr/engine.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/javascript/ngui/breadcrumbs.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/javascript/ngui/tree.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/javascript/ngui/coursemenu.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/javascript/dwr/util.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/groupjs/9F8F9394220E298DE46C9850F721D5AB.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/assignment/dwr_open/interface/UserDWRFacade.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/bb-social-learning-BB589b581008438/js/mybb.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/cloud-profiles/js/profile_access.js?b2=3800.0.0-rel.30+071ab51&v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/groupjs/9CCC71006413DAF5ADD41A2B207A7D2B.js?v=3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/assignment/dwr_open/interface/ToolActivityService.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/bb-gate-BB589b581008438/js/tool_service.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/privacy-disclosure/js/cookieConsent.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/bb-social-learning-BB589b581008438/js/social.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    <script type="text/javascript" src="/webapps/assignment/dwr_open/interface/ProfileProviderService.js?v=3800.0.0-rel.30+071ab51_3800.0.0-rel.30+071ab51"></script>
    </head>
  <body id="learn-oe-body" >
  
<h1 class="hideoff hideFromQuickLinks">Open Quick Links</h1><div id=quick_links_wrap><a id=quick_links_lightbox_link href="#" onclick="quickLinks.lightboxHelper.toggleLightbox(); return false;" role=button aria-haspopup=true tabindex=1 title="Open&#x20;Quick&#x20;Links">Quick Links</a></div><div id=quickLinksLightboxDiv class=hideoff aria-hidden=true style="display:none"><div class=ax-content><div class=content-lite><div id=quick_links_landmarks_section><h2 class=hideFromQuickLinks>Page Landmarks</h2><ul class=shortcut-list id=quick_links_landmark_list></ul></div><div id=quick_links_headings_section><h2 class=hideFromQuickLinks>Content Outline</h2><ul class=shortcut-list id=quick_links_heading_list></ul></div></div><div id=quick_links_hotkeys_section class=legend><h2 class=hideFromQuickLinks>Keyboard Shortcuts</h2><ul class=keycombos id=quick_links_hotkey_list></ul></div></div></div><h1 class="hideoff hideFromQuickLinks"></h1><div class=global-nav-bar-wrap><div class=global-nav-bar-wrap-mobile-nav><button class="hamburger hamburger--squeeze" type=button><span class=hamburger-box><span class=hamburger-inner></span></span></button></div><div class="global-nav-bar logout"><a id="topframe.logout.label" href="/webapps/login/?action=logout" target=_top class="nav-link logout-link" title=Logout> Logout</a></div><div id=global-nav class=global-nav-bar role=navigation data-preview=false><div class=hideoff>Global Menu</div><button id=global-nav-link class="nav-link u_floatThis-right" href="#global-nav-flyout" aria-haspopup=true aria-controls=global-nav-flyout tabindex=1 accesskey=m title="Open&#x20;Global&#x20;Navigation&#x20;Menu"><img src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/ng/default_profile_avatar.svg" alt="" id=global-avatar dataToolTitle="User Avatar Image" class=global-top-avatar /> Shirley Whitaker<span id=badgeTotal style="visibility: hidden" title=""><span class=hideoff id=badgeAXLabel>Activity Updates</span><span class=badge id=badgeTotalCount title=""></span></span><img src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/mybb/arrowDown-topnav.png" alt="Expand Global Nav" id=global-toggle-img class=global-toggle /></button><div id=global-nav-flyout class=flyout-menu style="display: none;"><ul id=bottomButtons class=bottom-buttons><li class=bottom-buttons-home><a id="topframe.home.label" href="http://www.faytechcc.edu/" target=_blank class=home title=Home> Home</a></li><li class=bottom-buttons-help><a id="topframe.help.label" href="#" onClick="globalNavigation.openHelpWindow('https://help.blackboard.com/Learn/Student');" class=help title=Help> Help</a></li></ul></div></div></div>
<!-- global_nav.jsp -->

<div id="globalNavPageNavArea">
    <table class="bouncer" summary="Top frame table" role="presentation">
      <tr>
        <td>
          <div class="topTabs bgBanner" id="topTabs">
  
            <div class="brandingImgWrap">
              <a href="http://www.faytechcc.edu/" target="_blank" title="Faytech Logo">
                <img  src="/branding/_1_1/bb-brand-logo-sm.jpg"  alt="Faytech Logo" title="Faytech Logo" class="bannerImage"/>
</a>
            </div>
  
            <div class="tabWrapper-right">
              <H2 CLASS="hideoff">Top Frame Tabs</H2>
              <table class="appTabs transparent" id="appTabList" summary="Tab List table" role="presentation">
                <tr>
                 <td id="Blackboard Desktop"  >
                      <a href="/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1" TARGET="_top"><span>Blackboard Desktop</span>
                        <span class="hideoff"> Tab 1 of 1</span>
                      </a>
                    </td>
                  </tr>
              </table>
              <div class="clearfloats"></div>
            </div>
            </div>
        </td>
      </tr>
    </table>
  </div>

<div id="globalNavPageContentArea">

<h2 class="hideoff">
 Current Location
</h2>

<div id="breadcrumbs" class="breadcrumbs clearfix ">
 <div class="breadcrumb-controls clearfix" id="breadcrumb_controls_id">





<div id="helpTextToggle" class="helpLink hidden">
  <a href="#" id="helpTextToggleLink" class="browseIcon">
	<img id="helpTextToggleImg" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images-ltr/ci/ng/small_help_on2.gif" alt="Turn help text off and on"/></a>
</div>
 <input type='hidden' name='showHelperSetting' id='showHelperSetting' value=''>
 </div>

 <div class="path  noToggle" role="navigation">
 <ol class="clearfix">
    	<li
    class="root coursePath"
        > <a href="/webapps/blackboard/execute/courseMain?course_id=_23504_1"  title="2020SP Web, Pgm, &amp; Db Foundation (CTI-110-0002)">        <span id="crumb_1">
                      2020SP Web, Pgm, & Db Foundation (CTI-110-0002)
                  </span>
      </a>      <div id="arrowContext_1"
         class="courseArrow"       onClick="page.ContextMenu.changeArrowInBreadcrumb(1, event );">
<span class="contextMenuContainer" style=" display: inline;" bb:menuGeneratorURL="/webapps/blackboard/execute/getCrossCourseMenuHTML?course_id=_23504_1" bb:navItem="" bb:contextParameters="" bb:menuOrder="" bb:overwriteNavItems="" bb:beforeShowFunc="">
   
  <a  id="cmlink_4c2b4b50b692443abd13e5dca0e9bbb0" onfocus="page.ContextMenu.LI(event, 'cmdiv_4c2b4b50b692443abd13e5dca0e9bbb0',false);" onmouseover="page.ContextMenu.LI(event, 'cmdiv_4c2b4b50b692443abd13e5dca0e9bbb0',false);" class="cmimg editmode jsInit  " href="#contextMenu" title="Course-to-Course Navigation"> <img src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/icons/cmlink_generic.gif" alt="Course-to-Course Navigation" ></a>
  <div id="cmdiv_4c2b4b50b692443abd13e5dca0e9bbb0" class="cmdiv" style="display: none;">
   <ul id="cmul0_4c2b4b50b692443abd13e5dca0e9bbb0"> 
    <li class="contextmenubar_top">
      <a href="#close" class="close-menu">
        <span class="close-contextmenu" data-icon="X" role="presentation" aria-hidden="true"></span>
        <img alt="Close Menu" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/ng/close_mini.gif"></a>
    </li>      
       </ul>   
  </div>
</span>
</div>    </li>
   	<li
        > <a href="/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4158770_1&mode=reset"  title="Assignments">        <span id="crumb_2">
                      Assignments
                  </span>
      </a>          </li>
   	<li
        > <a href="/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4193319_1&mode=reset"  title="Module 4">        <span id="crumb_3">
                      Module 4
                  </span>
      </a>          </li>
   	<li
        > <a href="/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4193324_1&mode=reset"  title="Tutorials">        <span id="crumb_4">
                      Tutorials
                  </span>
      </a>          </li>
   	<li
    class="placeholder"        >         <span id="crumb_5">
                      Review Submission History: P2T1- Sales Prediction
                  </span>
                </li>
  </ol>
 </div>

</div>

<div class="locationPane">
 <nav role="navigation" aria-label="Course Menu" id="navigationPane" class="navigationPane ">
 
 <div id="menuWrap" class="menuWrap" >
  <div id="puller" >
  <a id="menuPuller" class="clickpuller" title="Hide Course Menu" href="#">
   <img id="expander" alt="Hide Course Menu" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/spacer.gif"/>
  </a>
 </div>
<div class="menuWrap-inner">
  <div id="courseMenuPalette" class="navPalette listCm navPaletteExpCol"><div class="actionBarMicro clearfix"><h2 class="hideoff">Menu Management Options</h2><ul class="nav clearfix u_floatThis-right"><li id="refreshMenuLink" class="secondaryButton "><a href="#" title="Refresh"><span><img src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/ng/small_refresh.gif" alt="Refresh"></span></a></li><li id="courseMapButton" class="secondaryButton "><a href="#" title="Display Course Menu in a Window"><span><img src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/ng/small_new_window.gif" alt="Display Course Menu in a Window"></span></a></li></ul></div><div class="navPaletteContent"><h2 class="hideoff" tabindex="-1">Course Menu:</h2><div id="courseMenuPalette_paletteTitleHeading"><div class="navPaletteTitle"><h3><a href="#" role="button" aria-expanded="true" class="comboLink" aria-controls="courseMenuPalette_contents" title="Collapse 2020SP Web, Pgm, & Db Foundation (CTI-110-0002)" id="courseMenu_link">2020SP Web, Pgm, & Db Foundation (CTI-110-0002)</a></h3><h3><a href="/webapps/blackboard/execute/courseMain?course_id=_23504_1" target="" class="submenuLink" id="courseMenu_combo" title="Go to Course Entry Page"><img src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/icons/generic_dbl_arrow_right.gif" alt="Course Entry Page"></a></h3></div></div><ul id="courseMenuPalette_contents" class="courseMenu"><li id="paletteItem:_406868_1" class="clearfix "><a href="/webapps/blackboard/content/launchLink.jsp?course_id=_23504_1&tool_id=_135_1&tool_type=TOOL&mode=view&mode=reset" target="_self"><span title="Announcements">Announcements</span></a></li><li id="paletteItem:_406869_1" class="clearfix "><a href="/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4158767_1&mode=reset" target="_self"><span title="How This Course Works">How This Course Works</span></a></li><li id="paletteItem:_406870_1" class="clearfix "><a href="/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4158768_1&mode=reset" target="_self"><span title="The Syllabus">The Syllabus</span></a></li><li id="paletteItem:_406871_1" class="clearfix "><a href="/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4158769_1&mode=reset" target="_self"><span title="Instructor Information">Instructor Information</span></a></li><li id="paletteItem:_406872_1" class="clearfix divider"><hr></li><li id="paletteItem:_406873_1" class="clearfix "><a href="/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4158770_1&mode=reset" target="_self"><span title="Assignments">Assignments</span></a></li><li id="paletteItem:_406874_1" class="clearfix "><a href="/webapps/blackboard/content/launchLink.jsp?course_id=_23504_1&tool_id=_141_1&tool_type=TOOL&mode=view&mode=reset" target="_self"><span title="Discussion Board">Discussion Board</span></a></li><li id="paletteItem:_406875_1" class="clearfix "><a href="/webapps/blackboard/content/launchLink.jsp?course_id=_23504_1&tool_id=_155_1&tool_type=TOOL&mode=view&mode=reset" target="_self"><span title="My Grades">My Grades</span></a></li><li id="paletteItem:_406876_1" class="clearfix "><a href="/webapps/blackboard/content/launchLink.jsp?course_id=_23504_1&tool_id=_136_1&tool_type=TOOL&mode=view&mode=reset" target="_self"><span title="Email">Email</span></a></li><li id="paletteItem:_406877_1" class="clearfix divider"><hr></li><li id="paletteItem:_406878_1" class="clearfix "><a href="/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4158771_1&mode=reset" target="_self"><span title="Optional Resources">Optional Resources</span></a></li><li id="paletteItem:_406879_1" class="clearfix "><a href="https://www.faytechcc.edu/academics/blackboard-for-students/" target="_blank"><span title="Student Support">Student Support</span></a></li><li id="paletteItem:_406880_1" class="clearfix "><a href="https://www.faytechcc.edu/academics/blackboard-for-students/#policies" target="_blank"><span title="FTCC Policies">FTCC Policies</span></a></li><li id="paletteItem:_406881_1" class="clearfix "><a href="/webapps/blackboard/content/launchLink.jsp?course_id=_23504_1&tool_id=_9_1&tool_type=TOOL&mode=view&mode=reset" target="_self"><span title="Tools">Tools</span></a></li></ul></div></div><div id="myGroups" class="navPalette tools navPaletteExpCol"><div class="navPaletteContent"><div id="myGroups_paletteTitleHeading"><div class="navPaletteTitle"><h3><a href="#" role="button" aria-expanded="true" id="myGroups_link" aria-controls="myGroups_contents" title="Collapse My Groups"> My Groups </a></h3></div></div><ul id="myGroups_contents" class=""><li id="mygroups._58547_1"><h4><a class="comboLink" role="button" href="#" aria-controls="mygroups._58547_1_groupContents" id="mygroups._58547_1_groupExpanderLink" title="Expand CTI-110-0002 (CS171684)">CTI-110-0002 (CS171684)</a></h4><a class="submenuLink" href="/webapps/blackboard/execute/modulepage/viewGroup?course_id=_23504_1&group_id=_58547_1" title="Go to Group Homepage: CTI-110-0002 (CS171684)"><img alt="Group Homepage: CTI-110-0002 (CS171684)" src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/icons/generic_dbl_arrow_right.gif"></a><ul class="submenu" id="mygroups._58547_1_groupContents" style="display:none;"><li>&nbsp;</li></ul></li></ul></div></div>
  </div>
 </div>
 </nav>
 <div role="main" id="contentPanel" class="contentPane  ">
<div class="shadow">
       <div id="editmodeWrapper"> 
 
  <div id="content" class="contentBox ">
   
<div id="pageTitleDiv" class="pageTitle clearfix ">

  
<div id="pageTitleBar" class='pageTitleIcon' tabindex="0">
  <img src="https://learn.blackboardcdn.com/3800.0.0-rel.30+071ab51/images/ci/sets/set01/assignment_on.gif" alt="" id="titleicon"><h1 id="pageTitleHeader" tabindex="-1" ><span id="pageTitleText">
  Review Submission History: P2T1- Sales Prediction  </span></h1>
        <span id="_titlebarExtraContent" class="titleButtons"></span>
</div>



</div>

      <div class="container clearfix" id="containerdiv">
    <h2 class="hideoff">Content</h2>
    <script type="text/javascript" src="/webapps/achievements/js/achievement.js"></script><script src="/javascript/scriptaculous/version_pinned_scriptaculous.js"></script><link rel="stylesheet" href="/webapps/achievements/css/achievements.css" type="text/css" media="screen" /><script type="text/javascript">
new Ajax.Request('/webapps/achievements/checkAchievements.form', {
method:'get',
asynchronous:true,
parameters: {courseId: '_23504_1', type: 1 },
onSuccess: function(response) {
var jsonArray = response.responseJSON;
handleAchievements(jsonArray);
},
onFailure: function() { alert('Something went wrong...'); }
});
</script><div id="inlineGrader" class="inlineGrader ">
  
  <!-- Previewer - Left Panel -->
  <div id="previewer" class="previewer clearfix"> 

                <!-- Display the instruction and Alignment -->

      <!-- Toggle Button -->
      <div class="contentDetailsHeader">
       <h2> <a role="tab" class="" href="#" onclick="inlineGrading.gradingUtil.toggleOnEvent( event, $('contentDetails'), false, 'a' );" 
            title="Assignment Instructions Click to view/hide content" 
            aria-expanded=" false">
          <span>Assignment Instructions</span>
        </a></h2>
      </div>


     <!--  Tab Panel -->
    <div class="collapseTabs" id="contentDetails" style=" display:none;  ">
    
    <!-- Tabs -->
               <!--  Content  -->
         <div class="collapseTabsData" id="contentAreaBlock0">
                         <div id="instructionId" style="height:auto; overflow:visible;">
               <html>
 <head></head>
 <body>
  <div class="vtbegenerated">   
   <div class="vtbegenerated"> 
    <p><strong>Introduction:</strong></p> 
    <p>Guided tutorial on how to use the print and input functions</p> 
    <p><strong>Instructions:</strong></p> 
    <p>If you haven't already done so, review the <a target="_blank" href="https://mediaplayer.pearsoncmg.com/_cc_640x480/ph/streaming/esm/ecs_gaddis_sowpython_3/Chap02_Vid03_The_Sales_Prediction_Problem.mp4"><strong>Sales Prediction Program VideoNote</strong></a> for a guided tutorial on how to complete this assignment.</p> 
    <p>For <strong>Chapter 1: Input, Processing, and Output</strong> in your textbook, you will complete Exercise #2, VideoNote Performing Exercise 2 on page 74 and submit the finished code file through the assignment link in this folder.</p> 
    <ol> 
     <li><strong>Create</strong> a new Python code file named <strong>P2T1_<strong>S</strong>alesPrediction</strong><strong>_<strong><strong>LastnameFirstname</strong></strong>.py</strong></li> 
     <li>Add a&nbsp;<strong>title comment block</strong> to the top of the new Python file using the following form:<br><br> # A brief description of the project<br> # Date<br> # CTI-110 P2T1 - Sales Prediction<br> # Your Name<br> #<br><br></li> 
     <li>Using the <strong>VideoNote</strong> above as a guide, complete the programming challenge exercise #2 - Sales Prediction program at the end of chapter 1 on page 74.</li> 
     <li><strong>Submit</strong> your finished code solution file(s) through this assignment link by the posted deadline.</li> 
    </ol> 
    <p><strong>Grading Criteria:</strong></p> 
    <p>Refer to the grading criteria posted in the "<strong>Assignments tab</strong>"</p> 
   </div>  
  </div>
 </body>
</html>
             </div>
                               </div>
         
      </div>


    <!-- End displaying the instruction and Alignments -->
        


  	<div class="previewerInner clearfix" id="previewerInner">
  	  	
    <div id="loadingMessage" class="stream_show_more_data" style="">
    <div class="main-message" >Loading...</div>
    <div class="extras">Please wait while we render this file</div>
  </div>
  <div id="downloadPanel" class="submission download" style="display: none;">
    <div class="fileTile">
      <img src="/webapps/assignment/images/download-icon-large.png">
      <h5 id="downloadPanelFileName"></h5>
      <div class="extras" id="downloadPanelExtraMessage"></div>
      <a id="downloadPanelButton" href="#" class="download button-1" role="button">Download</a>
    </div>
  </div>


    </div>
  </div>

  <!-- GradingPanel - Right Panel -->
    <div id="gradingPanel" class="gradingPanel  clearfix">
  <div class="gradingPanelHeader">
  <h2><a role="button" class="detailsHeader" id="gradingPanelHeader" href="#" onclick="inlineGrading.gradingUtil.gradingPaneltoggleOnEvent( event, $('assignmentInfo'), false, 'a' );" title="Assignment Details Click to view/hide content" aria-expanded="false" aria-controls="aboutBlog">
    <span>Assignment Details</span>
  </a></h2>
</div>

<!-- Resize Controls -->
<div id="resizeControls" class="resizeControls expanded">
  <a id="maximizer_btn" class="maximizer_btn" role="button" href="#"
     onclick="inlineGrading.toggleMaximized( event );"
     title="Click to maximize/restore view"
     aria-label="Maximize" aria-pressed="false">
    Click to maximize/restore view
  </a>
  <a id="gradingPanelCollapse_btn" class="gradingPanelCollapse_btn expanded" role="button" aria-expanded="true"
     href="#" onclick="inlineGrading.toggleGradingPanel( event );"
     title="Click to collapse/expand grading panel"
     aria-controls=”gradingPanel”>
    Click to collapse/expand grading panel
  </a>
</div>

<div role="tabpanel" class="attempt gradingPanelSection" id="assignmentInfo" style="height:auto; overflow:visible;  display:none; ">
  <h3>Name</h3>
<p>P2T1- Sales Prediction</p>


</div>
<div id="aggregateGradeContainer" class="gradeHeader">

  <form id="aggregateGradeForm" name="aggregateGradeForm">    
  <h3>
    <label for="aggregateGrade">
      <span class="mainLabel" aria-hidden="true" role="presentation">
              Grade
            </span>
    
      <span class="subHeader" aria-hidden="true" role="presentation">Last Graded Attempt</span>    </label>
    
      </h3>       
  
      
  <div id="aggregateGradeContent" class="grade readOnly">
    
            <input id="aggregateGrade" type="text"  value="95.00"  maxlength="11" readOnly
           class="gradeEntry " title="Grade"  aria-describedby="aggregateGrade_pointsPossible" aria-label="Grade scored using last graded attempt" >

        
                                                   
          <span class="pointsPossible" id="aggregateGrade_pointsPossible">/100</span>
            
  </div>
  </form>
  
  
  
</div>

 
<div id="currentAttempt">  


    <div class="attemptHeader" id="currentAttempt_header" >
    
            <div class="attemptHeaderLabel"> 
      <h3 id="currentAttempt_label">
        <label for="currentAttempt_grade">
             <span class='mainLabel'>Attempt   </span>
                                <span class="subHeader  dateStamp ">
                        2/18/20 2:37 PM
                                              </span>
                  </label>
      </h3>
    </div>
    
                 <div class="grade readOnly">
    <!-- the following line needs a trailing space or it causes the input to overlap the attempt drop down -->     
      <input id="currentAttempt_grade" name="grade" class="gradeEntry" type="text" value="95.00" maxlength="11"
                            title="Attempt Grade"
                           readOnly               aria-describedby="currentAttempt_pointsPossible" > 
                         <span class="pointsPossible" id="currentAttempt_pointsPossible">/100</span> 
      
      
      
    </div>
    
        
  </div>
    
  
    <div id="currentAttempt_content" class="attemptContent" style="height: auto; overflow: visible;">    

            
         
        <div id="currentAttempt_gradeDataPanel" class="gradeSubmissionPanel" style="display:  none ">
    <!-- Following div added to fix the animation issue -->
    <div>
      
       
      
		        
      
                    
              
            
    </div>
    </div> 
    
            
        <div id="currentAttempt_submission" class="segment">
 
      <h4>Submission</h4>
 
      <ul id="currentAttempt_submissionList" class="filesList">
                <li>
          <a id="currentAttempt_attemptFile_1830529_1" class="attachment genericFile" href="#"
              onclick="gradeAssignment.inlineView( event, '_1830529_1', '_8193634_1' );" >
            <span style='word-break:break-all;word-wrap:break-word'>P2T1_SalesPrediction_WhitakerShirley.py</span>
          </a>
                    <div class="downloadFile">
                        <a class="dwnldBtn" href="/webapps/assignment/download?course_id=_23504_1&amp;attempt_id=_8193634_1&amp;file_id=_1830529_1&amp;fileName=P2T1_SalesPrediction_WhitakerShirley.py" role="button"></a>
                      </div>
                  </li>
              </ul>
  
    </div>
      
      
    
    <div id="currentAttempt_comments" class="segment" >
  <h4>
        Comments
      </h4>
  <div  class="feedbackWrapper">

  
  <div id="currentAttempt_feedback" class="comment">
  
          <span class="userInfo">Feedback to Learner</span>
      
          <span class="dateStamp">2/21/20 11:18 AM</span>
        
    <html>
 <head></head>
 <body>
  <div class="vtbegenerated">
   <p><span class="mceItemHidden">Why <span class="mceItemHiddenSpellWord"></span></span><span class="mceItemHidden">did you <span class="mceItemHiddenSpellWord"></span></span><span class="mceItemHidden">do <span class="mceItemHiddenSpellWord"></span></span><span class="mceItemHidden">the <span class="mceItemHiddenSpellWord"></span></span><span class="mceItemHidden">calculation <span class="mceItemHiddenSpellWord"></span></span>twice?<span class="mceItemHidden"><span class="mceItemHiddenSpellWord"></span>﻿</span><span class="mceItemHidden"><span class="mceItemHiddenSpellWord"></span></span><span class="mceItemHidden"><span class="mceItemHiddenSpellWord"></span>﻿</span><span class="mceItemHidden"><span class="mceItemHiddenSpellWord"></span>﻿</span><span class="mceItemHidden"><span class="mceItemHiddenSpellWord"></span>﻿</span><span class="mceItemHidden"><span class="mceItemHiddenSpellWord"></span>﻿</span><span class="mceItemHidden"><span class="mceItemHiddenSpellWord"></span>﻿</span><br data-mce-bogus="1"></p>
  </div>
 </body>
</html>
   
  </div>
      
</div>

</div>
  

  </div>
    
   

</div><div class="taskbuttondiv_wrapper">
<p class="taskbuttondiv" id="bottom_submitButtonRow">
			<input id="bottom_saveAsArtifactButton" class="button-2" type="button" name="bottom_saveAsArtifactButton" role="button" value="Save As Artifact" onclick="javascript:Portfolio.saveAsArtifact('bb.assignmentArtifactProvider','%7B%22content_id%22%3A%22_4193326_1%22%2C%22column_id%22%3A%22_850225_1%22%2C%22attempt_id%22%3A%22_8193634_1%22%2C%22group%22%3A%22false%22%7D', '_23504_1', '_534704_1');">
		<input  class="submit button-1" name="bottom_OK" type="submit" role="button" value="OK" onClick="document.location='/webapps/bb-mygrades-BB589b581008438/myGrades?course_id=_23504_1&stream_name=mygrades&is_stream=false&callback=course';">

</p>
</div>

</div>

</div>

   </div>
   
     </div>
   </div> 
   </div>
   </div>  
</div></div>
<script type='text/javascript'>var resizeIframeListener = window.addEventListener('message', function(e) {
    try {
        var postMessageData = e.data;
        if (postMessageData.messageType === "kms-transcript" && postMessageData.entryId !== undefined) {
            var items = Array.from(document.querySelectorAll(".liItem"));
            items.forEach(function(item) {
                var iframe = item.getElementsByTagName("iframe")[0];
                if (iframe !== undefined && iframe.getAttribute("src").indexOf(postMessageData.entryId) >= 0) {
                    iframe.style.height = "800px";
                    iframe.parentElement.style.height = "800px";
                }
            });
        }
    }
    catch(ex) {
        console.error("encountered error in kms communication", ex);
    }
});</script><script type='text/javascript'> if (!Array.prototype.includes) {
    Object.defineProperty(Array.prototype, 'includes', {
        value: function(searchElement, fromIndex) {
            var o = Object(this);
            var len = o.length >>> 0;
            if (len === 0) {
                return false;
            }
            var n = fromIndex | 0;
            var k = Math.max(n >= 0 ? n : len - Math.abs(n), 0);

            function sameValueZero(x, y) {
                return x === y || (typeof x === 'number' && typeof y === 'number' && isNaN(x) && isNaN(y));
            }

            while (k < len) {
                if (sameValueZero(o[k], searchElement)) {
                    return true;
                }
                k++;
            }

            return false;
        }
    });
}

/** this function IS used. see com/kaltura/bb/util/JspTopFrameStartHookHandler.java:48 **/
var replaceKalturaIframeTokens = function(contentIdsToReplace, courseId) {
    var contentItems = Array.prototype.slice.call(document.querySelectorAll('[id^="contentListItem"]'));
    contentItems = contentItems.filter(function(contentItem) {
        var contentId = contentItem.id.split(':')[1];
        return contentIdsToReplace.includes(contentId);
    });

    contentItems.forEach(function(contentItem) {
        var contentId = contentItem.id.split(':')[1];
        var innerIframes = Array.prototype.slice.call(contentItem.querySelectorAll('iframe'));
        var kalturaIframe = innerIframes.filter(function(iframeElement) {
            return iframeElement.src.indexOf('osv-kaltura') !== -1;
        });

        if(kalturaIframe.length !== 1) {
            return;
        }

        var kalturaIframeElement = kalturaIframe[0],
            iframeSrc = kalturaIframeElement.src;

        iframeSrc = iframeSrc
            .replace('course_id=', 'course_id_old=')
            .replace('course_id%3D', 'course_id_old%3D')
            .replace('content_id=', 'content_id_old=')
            .replace('content_id%3D', 'content_id_old%3D');
        iframeSrc += '&course_id=' + courseId + '&content_id=' + contentId;

        kalturaIframeElement.src = iframeSrc;
    });
};

var addCourseIdIfMissing = function (courseId) {
    var items = Array.from(document.querySelectorAll("a[href*='viewContent1_Iframe']"));
    items = items.concat(Array.from(document.querySelectorAll("a[href*='LtiMashupPlayIframeWrapper']")));
    items = items.concat(Array.from(document.querySelectorAll("iframe[src*='LtiMashupPlayIframeWrapper']")));
    items.forEach(function(videoLink) {
        var isIframe = (videoLink.tagName === 'IFRAME'); 
        var videoHref = isIframe ? videoLink.src : videoLink.href;
        var hrefParts = videoHref.split('&');
        var wrongCourseId = null;
        hrefParts.forEach(function(part){
           part = part.split('=');
           if (part.length > 1 && part[0] === 'course_id') {
               if (part[1] !== courseId) { wrongCourseId = part[1]; }           }
        });
        if (wrongCourseId !== null) { videoHref.replace(wrongCourseId, courseId) }
        if (videoHref !== undefined && videoHref.indexOf("course_id=") === -1) {
            videoHref += "&course_id=" + courseId;
            if (isIframe) {videoLink.src = videoHref}
            else {videoLink.href = videoHref;}
        }
    });
};</script><script type='text/javascript'>addCourseIdIfMissing('_23504_1')</script>



  <script type="text/javascript">page.bundle.addKey('inlineconfirmation.close','Close');page.bundle.addKey('inlineconfirmation.refresh','Refresh');page.bundle.addKey('hidden.link.close.menu','End of menu. Click to return to associated item.');page.bundle.addKey('hidden.link.close.form','End of form. Click to return to associated item.');page.bundle.addKey('lightbox.loading','Loading...');page.bundle.addKey('yt.stopped','Stopped:');page.bundle.addKey('yt.playing','Playing:');page.bundle.addKey('yt.cued','Cued:');page.bundle.addKey('yt.buffering','Buffering:');page.bundle.addKey('yt.paused','Paused:');page.bundle.addKey('yt.ended','Ended:');page.bundle.addKey('yt.play','Play');page.bundle.addKey('yt.pause','Pause');page.bundle.addKey('yt.mute','Mute');page.bundle.addKey('yt.unmute','Unmute');page.bundle.addKey('lightbox.overlay','{0} has been opened as a lightbox overlaying the current page.');page.bundle.addKey('display.playerControls','Player Controls');page.bundle.addKey('display.videoPlayerControls','Video Player Controls');page.bundle.addKey('display.play','Play');page.bundle.addKey('display.stop','Stop');page.bundle.addKey('display.volumeUp','Volume Up');page.bundle.addKey('display.volumeDown','Volume Down');page.bundle.addKey('display.mute','Mute');page.bundle.addKey('display.videoStatus','Video Status');page.bundle.addKey('display.closePlayerControls','Close Player Controls');page.bundle.addKey('display.embeddedVideoPlayer','Embedded Video Player');page.bundle.addKey('display.of','of');page.bundle.addKey('display.view.on.flickr','View Photo on Flickr');page.bundle.addKey('mashups.content.data.msg','We are unable to display the mashup content. This happens if the system detects an invalid URL. Remove the mashup item and try again to resolve this issue.');page.bundle.addKey('contextmenu.frame.title','Menu frame');page.bundle.addKey('frameset.contentframe.title','Content');page.bundle.addKey('common.pair.paren','{0} ({1})');page.bundle.addKey('attachment.conversion.in.progress','This file is being converted. The estimated wait time is {0} seconds. Please refresh the page after this time has elapsed to view the document or select \"Download\" to download the document to your device.');page.bundle.addKey('collab.grade.rubric.override.invalid.value','Error: A valid numeric value must be entered: Rubric Total Override.');page.bundle.addKey('rubric.grading.inline.loading','Rubric loading.  Please wait...');page.bundle.addKey('rubric.grading.inline.retrieve.error','Failed to request rubric data for grading inline.');page.bundle.addKey('rubric.grading.raw.total','Raw Total: {0} (of {1})');page.bundle.addKey('rubric.grading.override.total.view.only','The rubric total value of {0} has been overridden with a value of {1} out of {2}.');page.bundle.addKey('rubric.grading.change.number.points','Change the number of points out of {0} to:');page.bundle.addKey('rubric.grading.popup.retrieve.error','An error occurred while trying to load the rubric evaluation information. Please close the window and try loading the rubric again.');page.bundle.addKey('rubric.grading.save.error','An error occurred while trying to save the rubric evaluation information.');page.bundle.addKey('rubric.grading.rubric.id.not.specified.error','An error occurred when trying to load the rubric.  The rubric was not specified.');page.bundle.addKey('rubric.grading.list.position','{0} of {1}');page.bundle.addKey('rubric.association.type.non_grading','Used for Secondary Evaluation');page.bundle.addKey('rubric.association.type.grading','Used for Grading');page.bundle.addKey('rubric.grading.confirm.switch.grading.rubric','Use this rubric as the grading rubric?');page.bundle.addKey('rubric.grading.default.evaluatorTemplate','{0}:  {1}');page.bundle.addKey('aggregate_grade.revert.confirm','Revert override grade?');page.bundle.addKey('aggregate_grade.receipt.success','Success: data processed.');page.bundle.addKey('aggregate_grade.receipt.error','Error: unknown error occurred while processing data.');page.bundle.addKey('aggregate_grade.override.title','Override/revert');page.bundle.addKey('aggregate_grade.revert.title','Revert');page.bundle.addKey('aggregate_grade.overridden.title','Manual Override Grade');page.bundle.addKey('aggregate_grade.grade.input.label','Override Grade');page.bundle.addKey('attempt_grading.rubric.button.label','Rubric');page.bundle.addKey('attempt_grading.receipt.success','Success: data processed.');page.bundle.addKey('attempt_grading.receipt.error','Error: unknown error occurred while processing data.');page.bundle.addKey('attempt_grading.forced_draft_save.success','Success: Rubric evaluation was saved as a draft. Please click Submit to save this grade.');page.bundle.addKey('attempt_grading.grade.input.label','Attempt Grade');page.bundle.addKey('attempt_grading.rubric.receipt','Rubric evaluation completed');page.bundle.addKey('attempt_grading.rubric.submit','Save Rubric');page.bundle.addKey('attempt_grading.grade.clear.confirm','Clear attempt grade?');page.bundle.addKey('portfolio.saveAsArtifact.button.label.save','Save As Artifact');page.bundle.addKey('portfolio.saveAsArtifact.button.label.saving','Saving As Artifact');page.bundle.addKey('portfolio.saveAsArtifact.button.label.saved','Saved As Artifact');page.bundle.addKey('portfolio.saveAsArtifact.error','Failed to save as artifact.');page.bundle.addKey('coursemenu.show','Show Course Menu');page.bundle.addKey('coursemenu.hide','Hide Course Menu');page.bundle.addKey('dynamictree.expand','Expand');page.bundle.addKey('dynamictree.collapse','Collapse');page.bundle.addKey('dynamictree.expand.folder','Expand {0} tree folder');page.bundle.addKey('dynamictree.collapse.folder','Collapse {0} tree folder');page.bundle.addKey('dragdrop.accessible.error.chooseOption','Select an item first.');page.bundle.addKey('dragdrop.accessible.empty','No items available to reposition.');page.bundle.addKey('dragdrop.accessible.complete','Items have been reordered.');page.bundle.addKey('dragdrop.accessible.complete.nochange','No ordering changes made.');page.bundle.addKey('closeStr','Close');page.bundle.addKey('moreOptionsStr','Click to see options');page.bundle.addKey('hiddenStr','This link is hidden from students');page.bundle.addKey('emptyStr','This link has no content');page.bundle.addKey('entryPointChangeConfirmStr','The entry point will changed to the next available Content');page.bundle.addKey('subheaderColonStr','Subheader: {0}');page.bundle.addKey('confirmQuickEnrollStr','You will be given the role: {0}. Proceed?');page.bundle.addKey('enterSearchKeyStr','Enter Search Criteria.');page.bundle.addKey('courseWelcomePageLbTitle','Quick Setup Guide');page.bundle.addKey('expandCollapse.expand.section.nocolon','Expand');page.bundle.addKey('expandCollapse.collapse.section.nocolon','Collapse');page.bundle.addKey('expandCollapse.expand.section.param','Expand {0}');page.bundle.addKey('expandCollapse.collapse.section.param','Collapse {0}');page.bundle.addKey('optin.decline.confirm.existing','This will permanently remove your Blackboard profile. Continue?');page.bundle.addKey('optin.processing.error','An error occurred processing your request.');page.bundle.addKey('tool.activity.description','activity updates');page.bundle.addKey('accessDeniedMsg','Access Denied');page.bundle.addKey('breadcrumbs.expand','Click to expand the breadcrumbs');</script>
  <script type="text/javascript">
    document.observe("dom:loaded", function()
    {
      gradeAssignment.touchUp( false );
      gradeAssignment.annotationRendererUrl = 'https://annotation-renderer-us-east-1.saas.bbpd.io';
    });
    </script>
  
  <script type='text/javascript'>var courseId ='_23504_1';</script>
  <script type="text/javascript">
   var course_id = "_23504_1";
   var courseTitle = "2020SP Web, Pgm, & Db Foundation (CTI-110-0002)";
   var confirmDeleteMenuItemMsg = "Are you sure you want to delete this item?";
   var confirmQuickUnenrollMsg = "Any user data created while quick enrolled in this course will be deleted. Proceed?";
   var confirmQuickEnrollMsg = "You will be given the role: Instructor. Proceed?";
   var inNewWindow = false;
   var theCourseMenu;
 </script>
 
  <script type='text/javascript'>globalNavigation.init(); Event.observe(window, 'resize', globalNavigation.onResize);</script>
  <script type="text/javascript">
    page.bundle.addKey('globalnav.menu.expand','Expand\x20Global\x20Nav');
    page.bundle.addKey('globalnav.menu.collapse','Collapse\x20Global\x20Nav');

    function insertSkipLinkAfterBodyStart(referenceNode, newNode, linkContent)
    {
      if( top === self )
      {
        /* Evaluates if the page is not been loaded inside Iframe,
        only attach skip-link in original view, not Ultra, because ultra has his own skip link. */
        referenceNode.parentNode.insertBefore( newNode, referenceNode );
        newNode.innerHTML = linkContent;
      }
    }

    var skipLink = new Element('a',{id:'skip-to-content', href: '#content', tabIndex: '1'});
    var learnBody = document.body.firstChild;
    var linkContent = 'Skip\x20To\x20Content';
    this.insertSkipLinkAfterBodyStart(learnBody, skipLink, linkContent);
  </script>
  
  <script type="text/javascript">
    page.bundle.addKey('quick_links.link.title','Navigate\x20to\x20element\x20\x7B1\x7D\x20of\x20type\x20\x7B2\x7D\x20in\x20\x7B0\x7D\x20frame');
    page.bundle.addKey('quick_links.lightbox_title','Quick\x20Links');
    page.bundle.addKey('quick_links.link_title','Open\x20Quick\x20Links');
    page.bundle.addKey('quick_links.hotkey.shift','Shift');
    page.bundle.addKey('quick_links.hotkey.control','Ctrl');
    page.bundle.addKey('quick_links.hotkey.alt','Alt');
    page.bundle.addKey('quick_links.hotkey.combination_divider','\x2B');
  </script>
  
  <script type="text/javascript">quickLinks.initialize( [ 'null' ] );</script>
  <script type="text/javascript">
  		            globalNavMenu.init( true );
  		          </script>
  		        
  <script type='text/javascript'> social.Profile.MY_PROFILE_TOOL_ID='BB-CORE_____myProfile'; social.Profile.MY_PROFILE_TOOL_URI='/webapps/bb-social-learning-BB589b581008438/execute/mybb?cmd=display&toolId=BB-CORE_____myProfile&location='; </script>
 
   <script type="text/javascript">
   FastInit.addOnLoad( function()
   {
            if ( window.DWREngine )
       {
        try {DWREngine.beginBatch();} catch(ignore) {}
       } 
                page.decoratePageBanner();
                                                             attemptInlineGrader = new attemptGrading.inlineGrader( 'currentAttempt', '', '', '', 'false' );
                                                             attemptListInlineGrader = new inlineGraderList.keyboardAccessible( 'currentAttempt_attemptListButton', 'currentAttempt_attemptList' );
                                                             page.util.initPinBottomSubmitStep();
                                                             page.ContextMenu.hideMenuDiv('4c2b4b50b692443abd13e5dca0e9bbb0');
                                                             new page.PageHelpToggler(true, 'Help is On: Click to hide page help.', 'Help is Off: Click to show page help.', false );
                                                             breadcrumbs.rightMostNavItem = '';
                                                             breadcrumbs.rightMostParentURL = '/webapps/blackboard/content/listContent.jsp?course_id=_23504_1&content_id=_4193324_1&mode=reset';
                                                             new page.PageMenuToggler(true,'courseMenuToggle_23504_1', true);
                                                             courseMenu.nonceKey = 'blackboard.platform.security.NonceUtil.nonce.ajax';
                                                             courseMenu.nonceValue = '824c58e2-f1a5-478e-bd0a-99be2b432551';
                                                             new page.PaletteController('courseMenuPalette', 'courseMenu_link', false, false);
                                                             new page.ItemExpander('mygroups._58547_1_groupExpanderLink', 'mygroups._58547_1_groupContents', 'Expand', 'Collapse', true, '/webapps/bb-group-mgmt-LEARN/execute/group/getGroupMenuItems', 'course_id=_23504_1&group_id=_58547_1&newWindow=false&openInParentWindow=false', 'Expand CTI-110-0002 (CS171684)','Collapse CTI-110-0002 (CS171684)');
                                                             new page.PaletteController('myGroups', 'myGroups_link', false, false);
                                                             theCourseMenu = new courseMenu.CourseMenu('/webapps/blackboard/execute/doCourseMenuAction', '/webapps/blackboard/execute/getCourseMenuContextMenu');
                                                             tool_service.init ('300000', 'Suppress-Session-Timestamp-Update' );
                                                             if (typeof(initEditors) == 'function') { initEditors(); }; 
                                                             if (window['org'] && window['org']['owasp']) { org.owasp.esapi.ESAPI.initialize(); }; 
                                                             AllyIntegration.initJWT('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJBTExZIiwic3ViIjoiQUxMWV9UT0tFTiIsImZpbGVJZHMiOltdLCJjb3Vyc2VSb2xlIjoidW5wcml2aWxlZ2VkIiwiaXNzIjoiU09kS1NYWWFqeUVUM0pJY0tsYTA2MnhPWkl1bW15QngiLCJleHAiOjE1ODI2NTc2MjksImlhdCI6MTU4MjY1NzMyOSwiY291cnNlSWQiOiJfMjM1MDRfMSIsInVzZXJJZCI6Il81MzQ3MDRfMSJ9.nfxsB33R-aEay2irFC2XJ05YMOeuYrvTBmEFdRGLxEM');
                                                             AllyIntegration.initAllyJSConfigs('prod.ally.ac','2770');
                                                             jQuery.getScript('//' + window.ALLY_CFG.baseUrl + '/integration/learn/ally.js');
                                                             quickLinks.createHelper();
                                                                    window.profileAccess = new ProfileAccess( '/webapps/cloud-profiles/', 'https://api.cloudbb.blackboard.com/v1/sessions/redirectWithToken', 'https://ui.cloudbb.blackboard.com/profiles/me/edit?sid=7624acb1-a55d-4ba8-9d0d-c34a1f48b8db&source=learn', false, 'blackboard.platform.security.NonceUtil.nonce.ajax', '824c58e2-f1a5-478e-bd0a-99be2b432551' );
                                if ( window.DWREngine )
       {
         try {DWREngine.endBatch();} catch(ignore) {}
       }
                          BrowserSpecific.registerListeners();
                gradeAssignment.init('currentAttempt', '{"fileName":"P2T1_SalesPrediction_WhitakerShirley.py","viewUuid":"--nbv--618863068563","file_id":"_1830529_1","editMode":"false","viewUrl":"https://blackboard.ent.box.com/preview/expiring_embed/gvoct6FE!5CDBQaENoltZSOdMykhDM6VBa_k_fMiJ6qZjxPhVR82L6QVg3FMAE-XXfcLisdkG0nHSyAidQZ0itQRKs85JDaLM2vqe-74twA_ZawkG_i238gvUjZj1g-PMyhHYBswCM1w2jvoCnNNdRjsADrUyvCxPl8tYlyXlLmxsOc1XG_jUoOxDwOnHV3yvHRSI7pdeq5ylIvCJBm4L4vWr6epKrgf53Td3W55CdiKznZAwtnHNQ2xI2nVqhRqfTGQZ8wmaMx055nqH09KUm2j9fFNDRVMM01IHt9rHY9RCq1fZpoH1Y6jchkATOFOzoU79OQSXH5KlmgA79xJXbe9jbj0Hhu47gx82K7YN6tAWl9P5p6deaJNk6dVUzlgcEtIel4faWU2jTlTY6G04F1SbFCrDZf2w2pV2Uv2-xO9Tk4NzI1b39rcEojDc-FAMd2vbEkn1fW1L6TblBNoIzQvrgm4-fJDrvaPmKd0MchuvjlK-Jiux3ErTO0-e3E_gJXRzijT_U3AOAGJThbkv_2lSEkZJz3OEFFkB6MQ6HUOcHVT6-R2y48YLlDy0hQCWa1zNWjQF_i7N3gpvP8QajhkMj0T8s6hE6SQlzONuRfD4Q7zA5u5hWH8myd596VYjULv7PnL3ycOtaDoS3UOZVRke_SSYDkK0kCfMNh5X2dZUje94SsYsrVS2UPtidqHs01ui4MI5zjS2o36JTB3XA9svOHM9an1CUAlT6DevPG0Pff0gV4vumxC05gG1YZ9ugtT6u12SG1QAQareask_pJ4msXRJGNjNrz0chyibRmsA5tu1Ex4KesFBCMm475-3jWfaLXt8OkhI-EO6q4QI5dyVUpRh1jYPv-Qu6Eg-Y5-GqzWKR2GBtmxH2_bMlR3XXwuSch4koG1a42dc8lHcJeXUDl5cfB1DRFTGL0AjanEonQtVygxHUUTZB89sB-8CxBDLcFGpUbZBSJrAabkcIWoNN-__7FfrwMxcqerjDPWz92t_0v_Q2iq_f7vLnQ0me_KjCZntINuCFJUBR--hpQTFPyYdaGQHuCeUSHRzG370pqJUMz2txCxZ17K5zo9Xn7Zlfa_BmpuSpTcN-_6w6gKzWr2iV_-PQgHwKvREBhG0BJxjjh8Kii3pxk_Fn3gOKFarGjWaIW_C5EfsDj6lQcZ9cFUEfmRsZbBGuxcTBHEdddp4acGamtAyLAk_hHGzWIanMAT9ifFnSAxBQ-QCAUv5hhPE4iL02NicuNB2O6_KbJ4T4cyd8p9kqg..?showAnnotations=true&showDownload=false","downloadUrl":"/webapps/assignment/download?course_id=_23504_1&attempt_id=_8193634_1&file_id=_1830529_1&fileName=P2T1_SalesPrediction_WhitakerShirley.py","canDownloadWithAnnotation":"false","status":"CONVERTED"}');
               });
   </script>
       
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam.nr-data.net","licenseKey":"232bf20b67","agent":"","beacon":"bam.nr-data.net","applicationTime":832,"applicationID":"63650369","transactionName":"M1NbN0oCDxFYU0JaXAoZahNKCg8Fel9YR0ELWlUGSkw0ElVfV1dyF0VQBFYOBAxNc1ldRxZZVQ9dEU4RUV9Be1oXQlYRQQ==","queueTime":0}</script>
</body>
</html>
