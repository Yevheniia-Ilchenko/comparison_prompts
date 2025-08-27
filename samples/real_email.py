real_email_1= """Delivered-To: ilchenko.evheniia@gmail.com
Received: by 2002:a05:6200:b82:b0:5b4:3746:32ae with SMTP id dw2csp786248qnb;
        Tue, 26 Aug 2025 14:52:55 -0700 (PDT)
X-Google-Smtp-Source: AGHT+IFGNiewn67ze2H/p/bqzEWtPqmDGTkvJBcu2QgRn6tC+gRT43JH5NxTsJJoCFw7yE8687H3
X-Received: by 2002:a05:6a21:329c:b0:243:78a:82c6 with SMTP id adf61e73a8af0-2438fad2e95mr4665198637.27.1756245174953;
        Tue, 26 Aug 2025 14:52:54 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1756245174; cv=none;
        d=google.com; s=arc-20240605;
        b=OO3sLOie9XsJbWjDX9qV6mL+kyjGA/r+fw3lV3erCjC6QrNeZknFtX+GPWNWSfuuf/
         3htidh1jcTL3ply0jAQ9V4zUfOxeuQ1CPNnje+vRhchhtLzNi3Ke5tnS7vCWf1muHCaf
         Mg9iGKxwpi1XYyLACNEpvXwRzr11fyVLfy6YwNtHYFeLYEYTq22U2EHo77cYRlH8y+O+
         h0rNTZfndU5DTRwGswJzL1m+H7zTnGhtDGeKh1mhlcCxucif97WQ3G3c1a5tNjom+GR2
         sqlGnsNBTtFE8cZcBe/IV6zswr0sUw+AsriuFFpk7nu6Q5CLyAJ6ookjyYWg4r1XDup1
         P8kA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;
        h=precedence:list-unsubscribe-post:list-unsubscribe:feedback-id
         :reply-to:sesame_open:mime-version:subject:message-id:to:from:date
         :sender:dkim-signature;
        bh=fuuTK87X2SF8yR8l8iUheihN7ljEgInJwl32QZfLrDI=;
        fh=b26xgq3XgYinM+ZrMdQW71lBAjK2WC3KDt8bU6L0WEk=;
        b=I3mKAEIL/hXZqnpwfG/x4x5OKa+A9oadKPYq5xii7EgEhrY4oFtEj3TereeSwRflZJ
         gClclFt90zDpGsW6u4LirB7l8llSwDjieLVZrZWeh3qQHKl/BgMv3trvjEvI0GyUoOEP
         42JKNoCUhSZf/jcBcKcy9OyW/L3LAK0tSdIvN/6bvxTSQiCcexVnr8Ezg6Np9H+sDyuo
         cma08EXk9yGOrZrvIbN4HvqVL4Ioj1D7EKIsR/iHZ8CPctok11tOwwklZNYIAFD6qomV
         4rwZYL43yyFWQ3/6voQ0rOY9Lw4B+xFInpHxWBvVOFhoE+p+B04js7xDngzXX/xwIt3h
         mruw==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@sc.mail.deepseek.com header.s=mail header.b=E1+FYeZx;
       spf=pass (google.com: domain of support@sc.mail.deepseek.com designates 101.44.172.109 as permitted sender) smtp.mailfrom=support@sc.mail.deepseek.com;
       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=sc.mail.deepseek.com
Return-Path: <support@sc.mail.deepseek.com>
Received: from hwsg1c109.sendcloud.org (hwsg1c109.sendcloud.org. [101.44.172.109])
        by mx.google.com with ESMTPS id 41be03b00d2f7-b4c4301a597si244491a12.967.2025.08.26.14.52.54
        for <ilchenko.evheniia@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);
        Tue, 26 Aug 2025 14:52:54 -0700 (PDT)
Received-SPF: pass (google.com: domain of support@sc.mail.deepseek.com designates 101.44.172.109 as permitted sender) client-ip=101.44.172.109;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@sc.mail.deepseek.com header.s=mail header.b=E1+FYeZx;
       spf=pass (google.com: domain of support@sc.mail.deepseek.com designates 101.44.172.109 as permitted sender) smtp.mailfrom=support@sc.mail.deepseek.com;
       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=sc.mail.deepseek.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple;
 d=sc.mail.deepseek.com; i=@sc.mail.deepseek.com; q=dns/txt; s=mail;
 t=1756245173; h=sender : date : from : to : message-id : subject :
 mime-version : content-type : reply-to : list-unsubscribe : from :
 list-unsubscribe-post : feedback-id;
 bh=MrEA2qtpUQeSky0meD1py0vG/Ut8Z4HDnMZ48X+or7s=;
 b=E1+FYeZxvyLlnB2KQO/AFJQoJ7cJdVPDBv0zr3kdZ3+YivlWIbCBZp/gyEGwttVE9yH2r
 WPm4htRiJ3VWpiaw0lvwYrnfpV3kVDp+xhydbLwjYpTCSxLOtDu+tEXAWbOJTF3NRCAEUBs
 TkiVPqGUKOqJWOZFnxhbM1WSBgCBHyU=
Sender: support@sc.mail.deepseek.com
Received: (Haraka outbound); Mon, 25 Aug 2025 19:16:49 +0800
Received: from sendcloud.api (Unknown [127.0.0.1])         by SendCloud Inbound Server with ESMTPA id E02AEFF5-7378-4525-9C36-18D8D574AB51.1         envelope-from <support@sc.mail.deepseek.com> (authenticated bits=0); Mon, 25 Aug 2025 19:16:49 +0800
Date: Mon, 25 Aug 2025 19:16:49 +0800 (CST)
From: DeepSeek <support@sc.mail.deepseek.com>
To: ilchenko.evheniia@gmail.com
Message-ID: <1756120609556_213118_121057_1578.sc-10_9_6_181-inbound70@sc.mail.deepseek.com>
Subject: =?utf-8?q?=5BImportant_Correction=5D_Regarding_to_=22DeepSeek_API_Upgrade?=
 =?utf-8?q?d_to_DeepSeek-V3=2E1_=26_Pricing_Adjustment=22?=
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_18750268_1684681143.1756120609550"
sesame_open: 3de0be30478255bab0a4c78a5a664774
REPLY-TO: DeepSeek <support@sc.mail.deepseek.com>
X-SENDCLOUD-UUID: 1756120609556_213118_121057_1578.sc-10_9_6_181-inbound70$ilchenko.evheniia@gmail.com
X-SENDCLOUD-LOG: 1756120609556_213118_121057_1578.sc-10_9_6_181-inbound70$ilchenko.evheniia@gmail.com#ilchenko.evheniia@gmail.com#313085#213118#28377116#false#false#-1#-1#
X-SENDCLOUD-LOG-NEW: MTc1NjEyMDYwOTU1Nl8yMTMxMThfMTIxMDU3XzE1Nzguc2MtMTBfOV82XzE4MS1pbmJvdW5kNzAkaWxjaGVua28uZXZoZW5paWFAZ21haWwuY29tI2lsY2hlbmtvLmV2aGVuaWlhQGdtYWlsLmNvbSMzMTMwODUjMjEzMTE4IzI4Mzc3MTE2I2ZhbHNlI2ZhbHNlIy0xIy0xIw==
Feedback-ID: i2597540754:p0:1:sc_cn
List-Unsubscribe: <mailto:28377116_313085_1756120609556_213118_121057_1578.sc-10_9_6_181-inbound70@sc.mail.deepseek.com>, <https://etrack05.com/track/unsubscribe2.do?p=eNqFj80KwjAQhN8leIxhJ-lmtzffQySkfxqsLfh3Ed_dSg8ehYE5DPMNsw8IpGyNsQbCEZ4i1cwxeQRAEzyIJYFF3a3dglKdYoJiW6Zmfkyd0KaM7amfzrPrn4uXknfHSy6ja-fLgvUaRIBoLFkz5PHWf7cIrqocxDtQbX7Bqj_EjGbgikkyQ2KovEYVURWirsnNyujv19yeidfS623XR0t2-ACXSkKE>
List-Unsubscribe-Post: List-Unsubscribe=One-Click
Precedence: bulk


------=_Part_18750268_1684681143.1756120609550
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<!doctype html>
<html lang=3D"und" dir=3D"auto" xmlns=3D"http://www.w3.org/1999/xhtml" xmln=
s:v=3D"urn:schemas-microsoft-com:vml" xmlns:o=3D"urn:schemas-microsoft-com:=
office:office">

<head>
  <title>[Important Correction] Regarding to "DeepSeek API Upgraded to Deep=
Seek-V3.1 & Pricing Adjustment"</title>
  <!--[if !mso]><!-->
  <meta http-equiv=3D"X-UA-Compatible" content=3D"IE=3Dedge">
  <!--<![endif]-->
  <meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3DUTF-8">
  <meta name=3D"viewport" content=3D"width=3Ddevice-width, initial-scale=3D=
1">
  <style type=3D"text/css">
    #outlook a {
      padding: 0;
    }

    body {
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }

    table,
    td {
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }

    img {
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }

    p {
      display: block;
      margin: 13px 0;
    }

  </style>
  <!--[if mso]>
    <noscript>
    <xml>
    <o:OfficeDocumentSettings>
      <o:AllowPNG/>
      <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
    </xml>
    </noscript>
    <![endif]-->
  <!--[if lte mso 11]>
    <style type=3D"text/css">
      .mj-outlook-group-fix { width:100% !important; }
    </style>
    <![endif]-->
  <!--[if !mso]><!-->
  <link href=3D"https://fonts.googleapis.com/css?family=3DNoto+Sans:100,300=
,400,500,700,900" rel=3D"stylesheet" type=3D"text/css">
  <style type=3D"text/css">
    @import url(https://fonts.googleapis.com/css?family=3DNoto+Sans:100,300=
,400,500,700,900);

  </style>
  <!--<![endif]-->
  <style type=3D"text/css">
    @media only screen and (min-width:480px) {
      .mj-column-per-100 {
        width: 100% !important;
        max-width: 100%;
      }

      .mj-column-px-640 {
        width: 640px !important;
        max-width: 640px;
      }
    }

  </style>
  <style media=3D"screen and (min-width:480px)">
    .moz-text-html .mj-column-per-100 {
      width: 100% !important;
      max-width: 100%;
    }

    .moz-text-html .mj-column-px-640 {
      width: 640px !important;
      max-width: 640px;
    }

  </style>
  <style type=3D"text/css">
    @media only screen and (max-width:479px) {
      table.mj-full-width-mobile {
        width: 100% !important;
      }

      td.mj-full-width-mobile {
        width: auto !important;
      }
    }

  </style>
  <style type=3D"text/css">
    li::marker {
      color: #4d6bfe;
    }

    ol,
    ul {
      padding-left: 20px;
    }

    ol li,
    ul li {
      padding-bottom: 16px;
      line-height: 26px;
    }

    code {
      background-color: #afb8c133;
      color: rgb(31, 35, 40);
      padding: 4px;
      white-space: break-spaces;
      font-family: var(--fontStack-monospace, ui-monospace, SFMono-Regular,=
 SF Mono, Menlo, Consolas, Liberation Mono, monospace);
    }

  </style>
</head>

<body style=3D"word-spacing:normal;background-color:#F6F7FA;">
  <div style=3D"background-color:#F6F7FA;" lang=3D"und" dir=3D"auto">
    <!--[if mso | IE]><table align=3D"center" border=3D"0" cellpadding=3D"0=
" cellspacing=3D"0" class=3D"" role=3D"presentation" style=3D"width:900px;"=
 width=3D"900" ><tr><td style=3D"line-height:0px;font-size:0px;mso-line-hei=
ght-rule:exactly;"><![endif]-->
    <div style=3D"margin:0px auto;max-width:900px;">
      <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" style=3D"width:100%;">
        <tbody>
          <tr>
            <td style=3D"direction:ltr;font-size:0px;padding:0px;padding-to=
p:46px;text-align:center;">
              <!--[if mso | IE]><table role=3D"presentation" border=3D"0" c=
ellpadding=3D"0" cellspacing=3D"0"><tr></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align=3D"center" border=3D"0=
" cellpadding=3D"0" cellspacing=3D"0" class=3D"" role=3D"presentation" styl=
e=3D"width:900px;" width=3D"900" bgcolor=3D"#FFFFFF" ><tr><td style=3D"line=
-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style=3D"background:#FFFFFF;background-color:#FFFFFF;margin:0px au=
to;max-width:900px;">
      <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" style=3D"background:#FFFFFF;background-color:#FFF=
FFF;width:100%;">
        <tbody>
          <tr>
            <td style=3D"direction:ltr;font-size:0px;padding:0px;padding-le=
ft:10px;padding-right:10px;padding-top:65px;text-align:center;">
              <!--[if mso | IE]><table role=3D"presentation" border=3D"0" c=
ellpadding=3D"0" cellspacing=3D"0"><tr><td class=3D"" style=3D"vertical-ali=
gn:top;width:880px;" ><![endif]-->
              <div class=3D"mj-column-per-100 mj-outlook-group-fix" style=
=3D"font-size:0px;text-align:left;direction:ltr;display:inline-block;vertic=
al-align:top;width:100%;">
                <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" rol=
e=3D"presentation" style=3D"vertical-align:top;" width=3D"100%">
                  <tbody>
                    <tr>
                      <td align=3D"center" style=3D"font-size:0px;padding:0=
px;word-break:break-word;">
                        <table border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" role=3D"presentation" style=3D"border-collapse:collapse;border-spaci=
ng:0px;">
                          <tbody>
                            <tr>
                              <td style=3D"width:312px;">
                                <img alt=3D"DeepSeek Logo" src=3D"https://c=
dn.deepseek.com/logo_2.png" style=3D"border:0;display:block;outline:none;te=
xt-decoration:none;height:auto;width:100%;font-size:13px;" width=3D"312" he=
ight=3D"auto" />
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align=3D"center" border=3D"0=
" cellpadding=3D"0" cellspacing=3D"0" class=3D"" role=3D"presentation" styl=
e=3D"width:900px;" width=3D"900" bgcolor=3D"#ffffff" ><tr><td style=3D"line=
-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style=3D"background:#ffffff;background-color:#ffffff;margin:0px au=
to;max-width:900px;">
      <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" style=3D"background:#ffffff;background-color:#fff=
fff;width:100%;">
        <tbody>
          <tr>
            <td style=3D"direction:ltr;font-size:0px;padding:0px;padding-to=
p:40px;text-align:center;">
              <!--[if mso | IE]><table role=3D"presentation" border=3D"0" c=
ellpadding=3D"0" cellspacing=3D"0"><tr><td class=3D"" style=3D"vertical-ali=
gn:top;width:640px;" ><![endif]-->
              <div class=3D"mj-column-px-640 mj-outlook-group-fix" style=3D=
"font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-=
align:top;width:100%;">
                <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" rol=
e=3D"presentation" style=3D"vertical-align:top;" width=3D"100%">
                  <tbody>
                    <tr>
                      <td align=3D"center" style=3D"font-size:0px;padding:1=
0px 25px;word-break:break-word;">
                        <p style=3D"border-top:solid 1px #DFE3E8;font-size:=
1px;margin:0px auto;width:100%;">
                        </p>
                        <!--[if mso | IE]><table align=3D"center" border=3D=
"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"border-top:solid 1px #DFE3=
E8;font-size:1px;margin:0px auto;width:590px;" role=3D"presentation" width=
=3D"590px" ><tr><td style=3D"height:0;line-height:0;"> &nbsp;
</td></tr></table><![endif]-->
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align=3D"center" border=3D"0=
" cellpadding=3D"0" cellspacing=3D"0" class=3D"" role=3D"presentation" styl=
e=3D"width:900px;" width=3D"900" ><tr><td style=3D"line-height:0px;font-siz=
e:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style=3D"margin:0px auto;max-width:900px;">
      <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" style=3D"width:100%;">
        <tbody>
          <tr>
            <td style=3D"direction:ltr;font-size:0px;padding:0px;text-align=
:center;">
              <!--[if mso | IE]><table role=3D"presentation" border=3D"0" c=
ellpadding=3D"0" cellspacing=3D"0"><tr><td class=3D"" style=3D"vertical-ali=
gn:top;width:900px;" ><![endif]-->
              <div class=3D"mj-column-per-100 mj-outlook-group-fix" style=
=3D"font-size:0px;text-align:left;direction:ltr;display:inline-block;vertic=
al-align:top;width:100%;">
                <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" rol=
e=3D"presentation" width=3D"100%">
                  <tbody>
                    <tr>
                      <td style=3D"background-color:#FFFFFF;vertical-align:=
top;padding-top:10px;padding-right:40px;padding-left:40px;">
                        <table border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" role=3D"presentation" style=3D"" width=3D"100%">
                          <tbody>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:16px;font-weight:600;letter-spacing:0;line-height:22p=
x;text-align:left;color:#D32F2F;">[Important Correction] Regarding to "Deep=
Seek API Upgraded to DeepSeek-V3.1 & Pricing Adjustment"</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">Dear Developers,</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">First, we sincerely apologize for the ina=
ccuracies in our previous email regarding pricing information and the effec=
tive date. We deeply regret any confusion or inconvenience this may have ca=
used.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:600;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">Incorrect Information:</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">The previous email stated: "the price for=
 Output tokens: $1.12/million, effective from September 4, 2025, 16:00 UTC.=
"</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:600;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">Correct Information:</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">Pricing Adjustment<strong> (Effective Sep=
t. 5, 2025, 16:00 UTC)</strong>: <ul>
                                    <li>Input tokens: <strong>$0.07/million=
 (cache hit)</strong> / <strong>$0.56/million</strong> (cache miss)</li>
                                    <li>Output tokens: <strong>$1.68/millio=
n</strong></li>
                                    <li>The off-peak discount ends simultan=
eously</li>
                                  </ul> Current pricing remains until effec=
tive date. Please plan usage accordingly.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">Furthermore, to better meet your API need=
s, we have scaled up our service resources. You are encouraged to use the s=
ervice.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#4d6bfe;">Please be advised that the updated pricin=
g and effective date outlined in this email are final, <a style=3D"color: #=
4d6bfe" href=3D"https://api-docs.deepseek.com/quick_start/pricing">[View Pr=
icing Details]</a>.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">Thank you for your understanding and cont=
inued support.</div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align=3D"center" border=3D"0=
" cellpadding=3D"0" cellspacing=3D"0" class=3D"" role=3D"presentation" styl=
e=3D"width:900px;" width=3D"900" ><tr><td style=3D"line-height:0px;font-siz=
e:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style=3D"margin:0px auto;max-width:900px;">
      <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" style=3D"width:100%;">
        <tbody>
          <tr>
            <td style=3D"direction:ltr;font-size:0px;padding:0px;text-align=
:center;">
              <!--[if mso | IE]><table role=3D"presentation" border=3D"0" c=
ellpadding=3D"0" cellspacing=3D"0"><tr><td class=3D"" style=3D"vertical-ali=
gn:top;width:900px;" ><![endif]-->
              <div class=3D"mj-column-per-100 mj-outlook-group-fix" style=
=3D"font-size:0px;text-align:left;direction:ltr;display:inline-block;vertic=
al-align:top;width:100%;">
                <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" rol=
e=3D"presentation" width=3D"100%">
                  <tbody>
                    <tr>
                      <td style=3D"background-color:#FFFFFF;vertical-align:=
top;padding-top:18px;padding-right:40px;padding-left:40px;">
                        <table border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" role=3D"presentation" style=3D"" width=3D"100%">
                          <tbody>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">Best regards,</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">The DeepSeek Team</div>
                              </td>
                            </tr>
                            <tr>
                              <td align=3D"left" style=3D"font-size:0px;pad=
ding:10px 25px;word-break:break-word;">
                                <div style=3D"font-family:Noto Sans, Arial,=
 sans-serif;font-size:14px;font-weight:400;letter-spacing:0;line-height:22p=
x;text-align:left;color:#020E36;">August 25, 2025</div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align=3D"center" border=3D"0=
" cellpadding=3D"0" cellspacing=3D"0" class=3D"" role=3D"presentation" styl=
e=3D"width:900px;" width=3D"900" bgcolor=3D"#ffffff" ><tr><td style=3D"line=
-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style=3D"background:#ffffff;background-color:#ffffff;margin:0px au=
to;max-width:900px;">
      <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" style=3D"background:#ffffff;background-color:#fff=
fff;width:100%;">
        <tbody>
          <tr>
            <td style=3D"direction:ltr;font-size:0px;padding:0px;padding-to=
p:57px;text-align:center;">
              <!--[if mso | IE]><table role=3D"presentation" border=3D"0" c=
ellpadding=3D"0" cellspacing=3D"0"><tr><td class=3D"" style=3D"vertical-ali=
gn:top;width:640px;" ><![endif]-->
              <div class=3D"mj-column-px-640 mj-outlook-group-fix" style=3D=
"font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-=
align:top;width:100%;">
                <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" rol=
e=3D"presentation" style=3D"vertical-align:top;" width=3D"100%">
                  <tbody>
                    <tr>
                      <td align=3D"center" style=3D"font-size:0px;padding:1=
0px 25px;word-break:break-word;">
                        <p style=3D"border-top:solid 1px #DFE3E8;font-size:=
1px;margin:0px auto;width:100%;">
                        </p>
                        <!--[if mso | IE]><table align=3D"center" border=3D=
"0" cellpadding=3D"0" cellspacing=3D"0" style=3D"border-top:solid 1px #DFE3=
E8;font-size:1px;margin:0px auto;width:590px;" role=3D"presentation" width=
=3D"590px" ><tr><td style=3D"height:0;line-height:0;"> &nbsp;
</td></tr></table><![endif]-->
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align=3D"center" border=3D"0=
" cellpadding=3D"0" cellspacing=3D"0" class=3D"" role=3D"presentation" styl=
e=3D"width:900px;" width=3D"900" bgcolor=3D"#ffffff" ><tr><td style=3D"line=
-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style=3D"background:#ffffff;background-color:#ffffff;margin:0px au=
to;max-width:900px;">
      <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" style=3D"background:#ffffff;background-color:#fff=
fff;width:100%;">
        <tbody>
          <tr>
            <td style=3D"direction:ltr;font-size:0px;padding:0px;padding-bo=
ttom:50px;padding-top:40px;text-align:center;">
              <!--[if mso | IE]><table role=3D"presentation" border=3D"0" c=
ellpadding=3D"0" cellspacing=3D"0"><tr><td class=3D"" style=3D"vertical-ali=
gn:top;width:900px;" ><![endif]-->
              <div class=3D"mj-column-per-100 mj-outlook-group-fix" style=
=3D"font-size:0px;text-align:left;direction:ltr;display:inline-block;vertic=
al-align:top;width:100%;">
                <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" rol=
e=3D"presentation" style=3D"vertical-align:top;" width=3D"100%">
                  <tbody>
                    <tr>
                      <td align=3D"center" style=3D"font-size:0px;padding:1=
0px 25px;word-break:break-word;">
                        <div style=3D"font-family:Noto Sans, Arial, sans-se=
rif;font-size:14px;font-weight:400;letter-spacing:0;line-height:20px;text-a=
lign:center;color:rgba(2, 14, 54, 0.6);">=C2=A9 2025 DeepSeek. All Rights R=
eserved.</div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align=3D"center" border=3D"0=
" cellpadding=3D"0" cellspacing=3D"0" class=3D"" role=3D"presentation" styl=
e=3D"width:900px;" width=3D"900" ><tr><td style=3D"line-height:0px;font-siz=
e:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style=3D"margin:0px auto;max-width:900px;">
      <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" style=3D"width:100%;">
        <tbody>
          <tr>
            <td style=3D"direction:ltr;font-size:0px;padding:0px;padding-to=
p:46px;text-align:center;">
              <!--[if mso | IE]><table role=3D"presentation" border=3D"0" c=
ellpadding=3D"0" cellspacing=3D"0"><tr></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><![endif]-->
  </div>
<center><table cellpadding=3D"0" cellspacing=3D"0" border=3D"0" width=3D"10=
0%"><tbody><tr><td align=3D"center" style=3D"overflow:hidden;font-size:0;pa=
dding:0;margin:0;line-height:0;"><img width=3D"1" height=3D"1" style=3D"wid=
th:1px;height:1px" alt=3D"" src=3D"https://etrack05.com/track/open2/eNp9jrs=
OwiAYhd-FOFLyHyi3zfcwhiCCEmubWHUxvrvUDm5OZzi3b6egyGnOGGew2kCSIa-1CRIKcAESpG=
2Atk7MqQMFH0yAQ1fHw_QYj5Y2dUjnPF4mkZ9Na43b0zXWQaTp2malU9YChnHirMRhzssXQfS9g=
JUC5NnPWAqmOJ08lb40opL6nCIdjlJ5SNlw1lS-32K6kF5fXm--An-9f0D7D0t1Qp0=3D.gif"/=
></td></tr></tbody></table></center><center><table width=3D"100%" align=3D"=
center" style=3D"max-width:900px;margin:0 auto;width:100%;"><tbody><tr alig=
n=3D"center"></tr><tr align=3D"center"><td style=3D"border-top:1px #e5e5e5 =
solid;padding-top:15px;padding-bottom:15px;" width=3D"560"><table border=3D=
"0" cellspacing=3D"0" cellpadding=3D"0" align=3D"center"><tbody><tr><td sty=
le=3D"background-color:#ddd;border:1px #ddd solid;border-radius:4px;padding=
:3px 15px;text-align:center;"><a style=3D"color:#a6a6a6;background:#ddd;fon=
t-size:12px;text-decoration:none;" href=3D"https://etrack05.com/track/unsub=
scribe2.do?p=3DeNp9j70OwjAQg98lYkyjc9K7pBvvgVB0lAARpZX4WxDvTgGJkcmD5c_2KiBQ=
YmuMNYgs8CTUMUv2CEDK8CCOGRyTu_QNKHdZMhKaOm6m27iNtKhDfyjjcXLlPmututyftA6un04=
z1qcQIyDGkjU7HS7l3UVwbesQvQN15mc0-Ez5T5SCXWqDdom9zGNZQ1HdeKYoQUTNh1GuZ-2PxN=
_Q42m_j2Zv_QKvL0LV" target=3D"_blank" rel=3D"noopener">=E7=82=B9=E5=87=BB=
=E8=BF=99=E9=87=8C=E5=8F=96=E6=B6=88=E8=AE=A2=E9=98=85<br/>click to unsubsc=
ribe</a></td></tr></tbody></table></td></tr></tbody></table></center></body>

</html>
------=_Part_18750268_1684681143.1756120609550--



"""

real_email_2 = """Delivered-To: olena.vrasii@destilabs.com
Received: by 2002:a17:907:d043:b0:ad8:7f8c:7805 with SMTP id vb3csp113090ejc;
        Tue, 26 Aug 2025 22:04:15 -0700 (PDT)
X-Google-Smtp-Source: AGHT+IHSEqsKlAEW+Sv1FL3Bmb7MMWn/5nHi9002Jgjmnf4C6ooH8lZuf8fsLPSAbYjJyWk5OCKa
X-Received: by 2002:a05:622a:2587:b0:4b2:8ac4:ef53 with SMTP id d75a77b69052e-4b2aab41a84mr246544801cf.74.1756271055255;
        Tue, 26 Aug 2025 22:04:15 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1756271055; cv=none;
        d=google.com; s=arc-20240605;
        b=i4kt/e3hKDo18g63Wyo1igAbtCtLOgcqFWMGg6jv/xjResbrh4Cns2pxo/3su6EPlJ
         bQD6d4P2oSnM3+3i/YTdJ3cQQHMKI/TDVFCOJMRWRt9ZkDSVhhaU2+0kHheLLI2pPt3C
         spPSkXvaWp/EoNPV4smgA1rfi3frEToYRpEEiNhbr2QLUrjR4xGHvxJidVscgLQ/NY6F
         1DlBot/hHSIw7NAWe29LdcQWt9Y9AoawAzdb+DCgwAQZGKerEnIKL51fFxvQarPBOdHr
         14j9TZimI1ilv6DBBIxwerj4aycYDJ4OMvOe/fvXK4CV4Yoki06Dsx6hVvT7rojXPqIm
         4ezA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;
        h=feedback-id:list-unsubscribe-post:precedence:mime-version:subject
         :message-id:to:reply-to:from:date:list-unsubscribe:dkim-signature
         :dkim-signature;
        bh=YVWiCfkaSolYeWko5EOrmiBAeGUJe2hiP3h1s8tV4tg=;
        fh=wbnjtc8Dz9OgopGfRrQzKU1qnPEjJIKibs2ZPjLLtiE=;
        b=F0mCCQYmeT78gHhJJN4sFRsTzYakHHhxQ9OHWh3rFodFT3VN+6XwNBWWbd3p/087f4
         6K915K/Wd378H5bqJAo/LpbXnDiHcS9B3VJk+8YJmrsmCw9xsCcE5RfxOeXFRAbsFzHN
         cAjVvc4JT4LEtX6A5qwOt0r8ERLgjwX1VCJXMUdMyaM6WcUJE487lyPtQshF+4MJubbW
         qWx7qu90vciJC9BRpSKp/WKavVjHJmaJoLtFZPPPRORulm1llsUQacfKBN5LxXdhahbG
         UfDy+9KgW8BUVNnT+GnfK/15sc3B89nwIjE+4MK/b+DSuCY58XP8sOoo9IEeD0kwm8UJ
         J73w==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@bf01.hubspotstarter.net header.s=hs2 header.b=T4vjDM40;
       dkim=pass header.i=@gigradar.io header.s=hs1-19487605 header.b=RdLa5NvN;
       spf=pass (google.com: domain of 1axcgf3xirq6yz1peraqq43vga4ed723gixtdo@bf01.hubspotstarter.net designates 158.247.18.248 as permitted sender) smtp.mailfrom=1axcgf3xirq6yz1peraqq43vga4ed723gixtdo@bf01.hubspotstarter.net;
       dmarc=pass (p=REJECT sp=QUARANTINE dis=NONE) header.from=gigradar.io
Return-Path: <1axcgf3xirq6yz1peraqq43vga4ed723gixtdo@bf01.hubspotstarter.net>
Received: from bid46ru.bf01.hubspotstarter.net (bid46ru.bf01.hubspotstarter.net. [158.247.18.248])
        by mx.google.com with ESMTPS id d75a77b69052e-4b2b8dc68b1si44340821cf.325.2025.08.26.22.04.14
        for <olena.vrasii@destilabs.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);
        Tue, 26 Aug 2025 22:04:15 -0700 (PDT)
Received-SPF: pass (google.com: domain of 1axcgf3xirq6yz1peraqq43vga4ed723gixtdo@bf01.hubspotstarter.net designates 158.247.18.248 as permitted sender) client-ip=158.247.18.248;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@bf01.hubspotstarter.net header.s=hs2 header.b=T4vjDM40;
       dkim=pass header.i=@gigradar.io header.s=hs1-19487605 header.b=RdLa5NvN;
       spf=pass (google.com: domain of 1axcgf3xirq6yz1peraqq43vga4ed723gixtdo@bf01.hubspotstarter.net designates 158.247.18.248 as permitted sender) smtp.mailfrom=1axcgf3xirq6yz1peraqq43vga4ed723gixtdo@bf01.hubspotstarter.net;
       dmarc=pass (p=REJECT sp=QUARANTINE dis=NONE) header.from=gigradar.io
Received: by 172.16.191.120 with SMTP id a0b9znrox27ui21rt47jl1najb7ndof76goyym9wr67;
        Wed, 27 Aug 2025 05:03:58 GMT
DKIM-Signature: v=1; s=hs2; d=bf01.hubspotstarter.net; 
        i=@bf01.hubspotstarter.net; 
        h=sender:from:from:reply-to:to:to:cc:cc:subject:subject:list-unsubscribe:form-sub:feedback-id:list-unsubscribe-post; 
        a=rsa-sha256; c=relaxed/relaxed; 
        bh=YVWiCfkaSolYeWko5EOrmiBAeGUJe2hiP3h1s8tV4tg=; 
        b=T4vjDM40qKEw3jyetgjR8bhsIx/UkM/w0tdLpEgy1/hOaeTXfKS3jYihwxVWT3
         gbh3r9PXCiqRNbRZTljwBTVitD2ZYkJKlGoFpj01y2Fmm/iw1Fp/552g0AtM3SZ
         rxh/w0xWFw9L8THdxHsfme3pZs5ynKVJ9NhkmevgDc3DjTBHwn9/hum5eb6bwN/
         MhZzfduopPVIlyp8CZ5/wZIX++6n6eHe2TkUBXWIw4v4cHzFIAtEbPTT5AtXfYU
         eVuivq8nQ1lzgkekRCiS+C3/2WS960GQLxVVBjg8Fy3gupXgjlxecSVuLal/RUh
         3yQtMBQB4c0V/COlTYp4b77PD+Og==; q=dns/txt; t=1756271038; 
        x=1756533838;
DKIM-Signature: v=1; s=hs1-19487605; d=gigradar.io; 
        i=@gigradar.io; 
        h=sender:from:from:reply-to:to:to:cc:cc:subject:subject:list-unsubscribe:form-sub:feedback-id:list-unsubscribe-post; 
        a=rsa-sha256; c=relaxed/relaxed; 
        bh=YVWiCfkaSolYeWko5EOrmiBAeGUJe2hiP3h1s8tV4tg=; 
        b=RdLa5NvNGDt8jjsNXzWc6rISFxvI9vVFlNuZ7SBLpwIfj/7std1pxmiPOhiuTe
         wOssNh65d3lOpRoiJLNys7lgAhGIWdIW8sbS3eUHKQiqwPMBnNIjgDwYK1ZrbJ6
         yaU67oZya44EmjGTjvQvwzJvJ0+ekl2VDx8nZgRgpUVqozzWdwSq7aux4i8SLg1
         vMWR6mi3Xv4nkUtYWV59Uy+WDCjulCP4yIDDt6D0owCr2EcvCj4htJ2BR7DvPfK
         WIXRy9gsX5NyDvrzPdE22x6k6AmW0zhg3qGNJ1G1Me9aoVoeImBkCHGAKuLMroM
         oQkSbWSNRfzd3ZSQ7lumm8DZ+I2w==; q=dns/txt; t=1756271038; 
        x=1756533838;
Return-Path: <1axcgf3xirq6yz1peraqq43vga4ed723gixtdo@bf01.hubspotstarter.net>
X-HS-Cid: 1axfne5ozgv359hi19evg4squ91vx4ervml1vg
List-Unsubscribe: <mailto:1axdm5a4yq3pkn2tzf3zwynm2iz3zx8skf35i0@bf01.hubspotstarter.net?subject=unsubscribe>, <https://hs.gigradar.io/hs/subscription-preferences/v2/unsubscribe-all?data=W2nXS-N30h-ScW2363kc1S8X5PW3ZSyFW2RKbKZW1QcGjP2x_BT2W2KW3v61QzpFLW22WqFz3SL5PjW1Y_B902KBLVMW49z4lV47BZHtW2p78783gnl6dW1LgzB23NT5_ZW38mkQR2YylqkW2Kr4zp3yZXR_W3VYZqC2YMwFhW234LNX4kpVzhW2KMY4l24T4Y2W2CCVgM2r5BMrW4pH0hg2WrfLyW1Qv7Ds4t58YjW1Xcrwj2HC0FpW1NvNfL23l460W2RTYlp2TvkHRW3F9zHf4kmkFdW43Vncs1X2jtbW2PBM_R2-Jp7yW2w5Cly47CRsZW4fQ1H22x-mq9W3g6DJX41CDNSW2t1k_V3D-nSjW21hSnX2WhmqDW2PxT_J2w5GwCW2PNlDX3bcbpqW3GJzZs36CtQsW4hd0qG1BgYWRW2Tr4gD234Rr8W3LZhV_3LY5sDW3ZTPFT3f_7jSW2Rjd3M3Y1MFFW4tGzbQ47mXBbW3ZG-zj41rsRtW3HcRvZ3dfwpZW3JWHbs1BmxjgW2TxX4P2RC1bVW2PyLxd3Y28TPW3BM-5m1ZbP_WW21lmMw1BMPB-W2zQscC3ZtBXpW2CLSFz4mKHVLW2s_FZF3d7jHbW2-lhkB3_tPbLW4r8K4521nP6hW3R3zj-3brJDtf3bqwlc04>
Date: Wed, 27 Aug 2025 01:03:58 -0400
From: Korlan Tleubekova <korlan.tleubekova@gigradar.io>
Reply-To: korlan.tleubekova@gigradar.io
To: olena.vrasii@destilabs.com
Message-ID: <1756271037891.ef2a75ac-b8c0-4580-9479-4f084b2f9b2f@bf01.hubspotstarter.net>
Subject: =?utf-8?Q?=E2=80=9CProven_Tips_to_Succeed_on_Upwork:_Real_Story_from_?=
 =?utf-8?Q?an_Agency_Owner=E2=80=9D_event_TOMORROW_with_Toby_Fox-Mason!?=
MIME-Version: 1.0
Content-Type: multipart/alternative; 
	boundary="----=_Part_10180_618694464.1756271037984"
Precedence: bulk
X-Report-Abuse-To: abuse@hubspotstarter.net (see
 https://hubspotstarter.net/)
List-Unsubscribe-Post: List-Unsubscribe=One-Click
Feedback-ID: aelvy0n:aigi6mpi:aidf:HubSpot

------=_Part_10180_618694464.1756271037984
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: quoted-printable

Join us TOMORROW for a detailed breakdown on achieving success on Upwork.

Hi everyone! =F0=9F=91=8B

I know many of you keep asking - how do agencies actually break through on =
Upwork and scale beyond just a few contracts?

Well, this week we=E2=80=99re bringing in someone who=E2=80=99s done exactl=
y that and is ready to share his playbook.

Proven Tips to Succeed on Upwork: Real Story from an Agency Owner

Speaker: @Toby Fox-Mason (https://hs.gigradar.io/e3t/Ctc/GF+113/d2hM-B04/VX=
bGfc6jPTQcN4JJLk_jmGQpW1KLHGL5BKpBVN76MZ-v3l5QzW6N1vHY6lZ3lDW4KXThK8GwwPKW1=
PjfsK4kbZchVVz0Lq7qqM-9W25WrZc250PnNW4wXgb31CQ_5vVj3D0W7lPwJ5W5TK_XS6yJY6yW=
89t2PX4N6R74F5dD-0qMGw-W6z2Ds_8yRj2DW9j0Fv43Kk6NwW5XcT2M2gXbfqW5LlWPP5zv-7F=
W95CgVv39mPtHW2MN55K46XtvmW3-f3Lg3vSZv3W40zf304F0_0hW47cw7S4nftjHW56SmBM1fp=
qb4W1KYYXC774zvKW4wwttR6S3L-5W3QQnkH52yD69f3SY1g804 )  =E2=80=93 Founder of=
 Ashgrove AI, GigRadar client, and successful Upwork agency owner.

=F0=9F=8E=AFAgenda:

=E2=80=A2 Challenges he faced on Upwork

=E2=80=A2 How he overcame them

=E2=80=A2 Proven tips that helped him succeed on Upwork

=F0=9F=93=86When: Aug 28 | 12PM Kyiv | 5PM Bali | 5AM EST

=F0=9F=93=8DWhere: Zoom - click here to join (https://hs.gigradar.io/e3t/Ct=
c/GF+113/d2hM-B04/VXbGfc6jPTQcN4JJLk_jmGQpW1KLHGL5BKpBVN76MZ-b3l5QzW69sMD-6=
lZ3nLW5wkhgG84qp7yW1H2ScH3QM_Q8W1f87f55DhfM8W1cn1mQ6NXMvtW311Y3w6G5YPqN7Z5b=
hz2Dg8cN6RWCRNM2s19N75bMBH7ytFqW5kBJdJ7scwdvW6G-xjR5y29yNN4Rb_Y5xH8ddW998yr=
g5Swmj-W1VQ7Kd8S6StKVMNhgd8D_ht5W7cFDVM59VBpqW6NH3kB8f7wL1W7_4vM24wtL96W8F4=
kXM1sdSD3W3d1_Xd6Zj_shW5bWTzl3J7MRMf2hLlpY04 )  or add the event (https://h=
s.gigradar.io/e3t/Ctc/GF+113/d2hM-B04/VXbGfc6jPTQcN4JJLk_jmGQpW1KLHGL5BKpBV=
N76MZ-b7hbQYW69tBBd6lZ3lWW9gvXpc6DvxH5W94Jh309b_m39W1nxprC8mgwstW3Q7tCk5qjp=
vNW3bs8l384DygPN1vZlpRKg4s5Vl49fD7VqmhdW3dlNVz8SrX8BN5J4dK46sH-KW1v5FbL6nnw=
9MW3__f9L5DlC3qMxHmbzkjX86N607rqNzDv8MW6tqmV75GL-tVW4XWHl35WQ4ydW6d6jxk486R=
RJW6W4y_S2yYT51W7sx36-8SwHHQVS_xRH1R2rw3N234tNrmqBDJW4NQdSf6HMRyjW6YRxGM8qz=
tZdW51C8Ch2YmMlnW5jtHkh1slSRZW1YbXhD174syFW38sgKG4vWq6-W1SlG832tnbmgW6s95kc=
3dR4BtW7gCTsS4B0qC7W7Xg2H54LPpP4W6yjSYQ3Cwp4XVkcg0M6jt3hcW989hk64RmrBXW5Hkw=
Vp8KZhYVW6K3_NP8tNp_NW75Z9fP4TxDlwW8SBZ2t3FqVJxVmDr184_RFRHW182Ny22_x1BzW48=
jBBQ7THjNHVd915d21Xz4BW7VCT3T7--tsPW8nzfsq1yk05TN576qJhNJlVHW7P6P1X6n_vvjW9=
bCRCj5BPFDHW6774WH5Hzlf6W4MtVLX5_fKyfW64h4Ls5Pq71LV10Vs97hQbR2MN_XGbRnLN0N1=
sD-61KwL8Xf6xDjkl04 )  to your calendar!

SUBSCRIBE (https://hs.gigradar.io/e3t/Ctc/GF+113/d2hM-B04/VXbGfc6jPTQcN4JJL=
k_jmGQpW1KLHGL5BKpBVN76MZ-v5jGjMW6N1X8z6lZ3lGW8lrb7F4mXVZ0W310Nsj68NKMGN7z5=
rhRKHt0vW91wywJ2Ln9MMW2Kn5zS8ZGk3lW8-30K12SD9kxW3D54Wr65lSmYW4JmxJS3Gn6PbW2=
BWVXC86_KnkW30k2FR3RSzS3VBtKXD76QBJdW3XRV5S8jjk5KW2x57jF6S9v5SW5qD7r975_RNg=
W6twq2V3Qgr9LW9jNVnc3mRNGGW6D3ytb42-q-DMRDrGKqlKjqW3C7Q1r5Z41VbW8CZYY82gLY0=
8W2gXKX73PFRtBW2wdWbV60_n1_Vh18Cx55njnPW7jHk4y5hShS4W6MT7LP8Z0Q4RW5cjH2V4M_=
qtwW4qRgh81tNLyZW6Sphww1NyXHMW4vLNqg1RhH29W1TpY9w6FVCLwW7THfp23T1yNWW5v4p4V=
8T9fRyW5XCj5y4rmMMnN4RYpfywhyhGW7Yd7WL4CfmkzN1pmvNyB7YsnVq3-mG7JgRnGW3Pdkc2=
3K7ySxf6bnKj804 )  to our Community Events calendar to stay updated on upco=
ming events

Don=E2=80=99t miss this chance to learn from a real Upwork success story!

SUBSCRIBE TO THE EVENT CALENDAR
(https://hs.gigradar.io/e3t/Ctc/GF+113/d2hM-B04/VXbGfc6jPTQcN4JJLk_jmGQpW1K=
LHGL5BKpBVN76MZ-v5jGjMW6N1X8z6lZ3lGW8lrb7F4mXVZ0W310Nsj68NKMGN7z5rhRKHt0vW9=
1wywJ2Ln9MMW2Kn5zS8ZGk3lW8-30K12SD9kxW3D54Wr65lSmYW4JmxJS3Gn6PbW2BWVXC86_Kn=
kW30k2FR3RSzS3VBtKXD76QBJdW3XRV5S8jjk5KW2x57jF6S9v5SW5qD7r975_RNgW6twq2V3Qg=
r9LW9jNVnc3mRNGGW6D3ytb42-q-DMRDrGKqlKjqW3C7Q1r5Z41VbW8CZYY82gLY08W2gXKX73P=
FRtBW2wdWbV60_n1_Vh18Cx55njnPW7jHk4y5hShS4W6MT7LP8Z0Q4RW5cjH2V4M_qtwW4qRgh8=
1tNLyZW6Sphww1NyXHMW4vLNqg1RhH29W1TpY9w6FVCLwW7THfp23T1yNWW5v4p4V8T9fRyW5XC=
j5y4rmMMnN4RYpfywhyhGW7Yd7WL4CfmkzN1pmvNyB7YsnVq3-mG7JgRnGW3Pdkc23K7ySxf6bn=
Kj804 )

GigRadar, 2810 N Church St PMB 94094, Wilmington, DE 19802-4447, US

Unsubscribe (https://hs.gigradar.io/hs/email-subscriptions/preferences/en/u=
nsubscribe?data=3DW2nXS-N30h-y_W3VHKmP2RtPm3W3F8n2l2CHzzwW3gqXsc3GS6cpW3_Ym=
8538ChZWW4tz5ph2r2M_6W34CgMQ1LdVgfW1VgYyD3Z_VCnW2KnXmG4pGywQW49xxdS3zkXqpW4=
pl7JS41QtC_W1VjbBR20T2_WW3N-Rkp41qDYKW32F8pZ3yN7JMW25jJtP2CVn_lW2HPQp638BrJ=
hW45BmrY2vLdvxW41XDhD1_mk9-W3F7wfm2vyGBNW2PFMy12TPb88W47xdxg1_f2T4W41FhkM38=
vVTJW2xYKb72Fz_gBW2FVydQ41KTL1W47vBqk4hKf_TW3P23F632m8-LW20Z7rl3NWzLNW3yW9R=
q3LJzN4W38CCsD2-DGXRW2-v_hN2sMG2_W1LF8543Z-zzMW4klrlT3yWZPmW4p9nTL2r8CfyW38=
mPS12TsNBcW3NLYvn30b7MnW3dwFXR1YW_2WW2RJrnK1-YvrCW4mlGhX3R41f5W1Q0R0-34kF95=
W2r4Q9n3LYTgJW4pl24T4ktzB1W4pHry21BmZF4W3_rGD93Kd7TXW36ll502p0rtCW2Kz8Rf23q=
L0TW4r6C1X2PM3bdW32sBvr1_sMJxW2FS50B2PS_xzW2-lg-k4kfTMCW1_pnrt23fz22W1NzygM=
2PNp4zW2nJqX62YK24S0&_hsenc=3Dp2ANqtz-9UGpur42pyVXk_cpF1K0hHDQ5bkvHSWvTq32O=
d02EmJ4bfGzJzmPNDdAXp5q_YeltCjcTb90dyLNG2m77JvEu2NhZRHBUfZLGMifF1QCUceNWnGg=
U&_hsmi=3D377743076 )
Manage preferences (https://hs.gigradar.io/hs/email-subscriptions/preferenc=
es/en/manage?data=3DW2nXS-N30h-y_W3VHKmP2RtPm3W3F8n2l2CHzzwW3gqXsc3GS6cpW3_=
Ym8538ChZWW4tz5ph2r2M_6W34CgMQ1LdVgfW1VgYyD3Z_VCnW2KnXmG4pGywQW49xxdS3zkXqp=
W4pl7JS41QtC_W1VjbBR20T2_WW3N-Rkp41qDYKW32F8pZ3yN7JMW25jJtP2CVn_lW2HPQp638B=
rJhW45BmrY2vLdvxW41XDhD1_mk9-W3F7wfm2vyGBNW2PFMy12TPb88W47xdxg1_f2T4W41FhkM=
38vVTJW2xYKb72Fz_gBW2FVydQ41KTL1W47vBqk4hKf_TW3P23F632m8-LW20Z7rl3NWzLNW3yW=
9Rq3LJzN4W38CCsD2-DGXRW2-v_hN2sMG2_W1LF8543Z-zzMW4klrlT3yWZPmW4p9nTL2r8CfyW=
38mPS12TsNBcW3NLYvn30b7MnW3dwFXR1YW_2WW2RJrnK1-YvrCW4mlGhX3R41f5W1Q0R0-34kF=
95W2r4Q9n3LYTgJW4pl24T4ktzB1W4pHry21BmZF4W3_rGD93Kd7TXW36ll502p0rtCW2Kz8Rf2=
3qL0TW4r6C1X2PM3bdW32sBvr1_sMJxW2FS50B2PS_xzW2-lg-k4kfTMCW1_pnrt23fz22W1Nzy=
gM2PNp4zW2nJqX62YK24S0&_hsenc=3Dp2ANqtz-9UGpur42pyVXk_cpF1K0hHDQ5bkvHSWvTq3=
2Od02EmJ4bfGzJzmPNDdAXp5q_YeltCjcTb90dyLNG2m77JvEu2NhZRHBUfZLGMifF1QCUceNWn=
GgU&_hsmi=3D377743076 )
------=_Part_10180_618694464.1756271037984
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www=
.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns=3D"http://www.w3=
.org/1999/xhtml" xmlns:o=3D"urn:schemas-microsoft-com:office:office" xmlns:=
v=3D"urn:schemas-microsoft-com:vml" lang=3D"en"><head>
    <title>=E2=80=9CProven Tips to Succeed on Upwork: Real Story from an Ag=
ency Owner=E2=80=9D event TOMORROW with Toby Fox-Mason!</title>
    <meta property=3D"og:title" content=3D"=E2=80=9CProven Tips to Succeed =
on Upwork: Real Story from an Agency Owner=E2=80=9D event TOMORROW with Tob=
y Fox-Mason!">
    <meta name=3D"twitter:title" content=3D"=E2=80=9CProven Tips to Succeed=
 on Upwork: Real Story from an Agency Owner=E2=80=9D event TOMORROW with To=
by Fox-Mason!">
   =20
   =20
   =20
<meta name=3D"x-apple-disable-message-reformatting">
<meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3DUTF-8">
<meta http-equiv=3D"X-UA-Compatible" content=3D"IE=3Dedge">
<meta name=3D"viewport" content=3D"width=3Ddevice-width, initial-scale=3D1.=
0">
    <!--[if gte mso 9]>
  <xml>
    <o:OfficeDocumentSettings>
      <o:AllowPNG/>
      <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
    <w:WordDocument xmlns:w=3D"urn:schemas-microsoft-com:office:word">
      <w:DontUseAdvancedTypographyReadingMail/>
    </w:WordDocument>
  </xml>
 =20
  <style>
    ul > li {
      text-indent: -1em;
    }
  </style>
<![endif]-->
<!--[if mso]>
<style type=3D"text/css">
 body, td {font-family: Arial, Helvetica, sans-serif;}
 .hse-body-wrapper-table {background-color: #ffffff;}
</style>
<![endif]-->
<!--[if mso | IE]>
  <style type=3D"text/css">
    .hse-column-container { border: none !important; padding: 0 !important;=
 }
  </style>
<![endif]-->
   =20
     =20
 =20
 =20
   =20
  <meta name=3D"generator" content=3D"HubSpot"><meta property=3D"og:url" co=
ntent=3D"https://hs.gigradar.io/-temporary-slug-7edda84a-d18a-4882-994e-dc6=
9560e49af"><meta name=3D"robots" content=3D"noindex,follow"><!--[if !((mso)=
|(IE))]><!-- --><style type=3D"text/css">@media only screen and (max-width:=
639px){img.stretch-on-mobile,.hs_rss_email_entries_table img,.hs-stretch-ct=
a .hs-cta-img{height:auto !important;width:100% !important}
.display_block_on_small_screens{display:block}.hs_padded{padding-left:20px =
!important;padding-right:20px !important}
.hs-hm,table.hs-hm{display:none}.hs-hd{display:block !important}table.hs-hd=
{display:table !important}
}@media only screen and (max-width:639px){.hse-border-m{border-left:1px sol=
id #ccc !important;border-right:1px solid #ccc !important;box-sizing:border=
-box}
.hse-border-bottom-m{border-bottom:1px solid #ccc !important}.hse-border-to=
p-m{border-top:1px solid #ccc !important}
.hse-border-top-hm{border-top:none !important}.hse-border-bottom-hm{border-=
bottom:none !important}
}.moz-text-html .hse-column-container{max-width:600px !important;width:600p=
x !important}
.moz-text-html .hse-column{display:table-cell;vertical-align:top}.moz-text-=
html .hse-section .hse-size-12{max-width:600px !important;width:600px !impo=
rtant}
@media only screen and (min-width:640px){.hse-column-container{max-width:60=
0px !important;width:600px !important}
.hse-column{display:table-cell;vertical-align:top}.hse-section .hse-size-12=
{max-width:600px !important;width:600px !important}
}@media only screen and (max-width:639px){.hse-body-wrapper-td{padding-top:=
20px !important}
#section-0 .hse-column-container{padding-top:0px !important;padding-bottom:=
0px !important}
#section-0 .hse-column-container{background-color:#fff !important} }@media =
only screen and (max-width:639px){.hse-body-wrapper-td{padding-bottom:20px =
!important}
#section-1 .hse-column-container{padding-top:0px !important;padding-bottom:=
0px !important;background-color:transparent !important}
#section-1 .hse-column-container{background-color:transparent !important} }=
</style><!--<![endif]--><style type=3D"text/css">#hs_body #hs_cos_wrapper_m=
ain a[x-apple-data-detectors]{color:inherit !important;text-decoration:none=
 !important;font-size:inherit !important;font-family:inherit !important;fon=
t-weight:inherit !important;line-height:inherit !important}
a{text-decoration:underline}p{margin:0}body{-ms-text-size-adjust:100%;-webk=
it-text-size-adjust:100%;-webkit-font-smoothing:antialiased;moz-osx-font-sm=
oothing:grayscale}
table{border-spacing:0;mso-table-lspace:0;mso-table-rspace:0}table,td{borde=
r-collapse:collapse}
img{-ms-interpolation-mode:bicubic}p,a,li,td,blockquote{mso-line-height-rul=
e:exactly}</style></head>
  <body id=3D"hs_body" bgcolor=3D"#ffffff" style=3D"margin:0 !important; pa=
dding:0 !important; font-family:Arial, sans-serif; font-size:15px; color:#2=
3496d; word-break:break-word">
    <div id=3D"preview_text" style=3D"display:none;font-size:1px;color:#fff=
fff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;=
" lang=3D"en">Join us TOMORROW for a detailed breakdown on achieving succes=
s on Upwork.</div>
   =20
<!--[if gte mso 9]>
<v:background xmlns:v=3D"urn:schemas-microsoft-com:vml" fill=3D"t">
    <v:fill type=3D"tile" size=3D"100%,100%" color=3D"#ffffff"/>
</v:background>
<![endif]-->
    <div class=3D"hse-body-background" lang=3D"en" style=3D"background-colo=
r:#ffffff" bgcolor=3D"#ffffff">
      <table role=3D"presentation" class=3D"hse-body-wrapper-table" cellpad=
ding=3D"0" cellspacing=3D"0" style=3D"margin:0; padding:0; width:100% !impo=
rtant; min-width:320px !important; height:100% !important" width=3D"100%" h=
eight=3D"100%">
        <tbody><tr>
          <td class=3D"hse-body-wrapper-td" valign=3D"top" style=3D"font-fa=
mily:Arial, sans-serif; font-size:15px; color:#23496d; word-break:break-wor=
d; padding-top:20px; padding-bottom:20px">
            <div id=3D"hs_cos_wrapper_main" class=3D"hs_cos_wrapper hs_cos_=
wrapper_widget hs_cos_wrapper_type_dnd_area" style=3D"color: inherit; font-=
size: inherit; line-height: inherit;" data-hs-cos-general-type=3D"widget" d=
ata-hs-cos-type=3D"dnd_area">  <div id=3D"section-0" class=3D"hse-section h=
se-section-first" style=3D"padding-left:10px; padding-right:10px">
   =20
   =20
      <div class=3D"hse-column-container" style=3D"min-width:280px; max-wid=
th:600px; margin:0 auto; background-color:#ffffff" bgcolor=3D"#ffffff">
   =20
    <!--[if (mso)|(IE)]>
      <table align=3D"center" style=3D"width:600px;" cellpadding=3D"0" cell=
spacing=3D"0" role=3D"presentation" width=3D"600" bgcolor=3D"#ffffff">
      <tr style=3D"background-color:#ffffff;">
    <![endif]-->
    <!--[if (mso)|(IE)]>
  <td valign=3D"top" style=3D"width:600px;">
<![endif]-->
<!--[if gte mso 9]>
  <table role=3D"presentation" width=3D"600" cellpadding=3D"0" cellspacing=
=3D"0" style=3D"width:600px">
<![endif]-->
<div id=3D"column-0-0" class=3D"hse-column hse-size-12">
  <div id=3D"hs_cos_wrapper_module_17550191305201" class=3D"hs_cos_wrapper =
hs_cos_wrapper_widget hs_cos_wrapper_type_module" style=3D"color: inherit; =
font-size: inherit; line-height: inherit;" data-hs-cos-general-type=3D"widg=
et" data-hs-cos-type=3D"module"><table class=3D"hse-image-wrapper" role=3D"=
presentation" width=3D"100%" cellpadding=3D"0" cellspacing=3D"0">
  <tbody>
    <tr>
      <td class=3D"hs_padded" align=3D"center" valign=3D"top" style=3D"font=
-family:Arial, sans-serif; color:#23496d; word-break:break-word; text-align=
:center; padding:10px 20px; font-size:0px">
        <img alt=3D"Frame 34-3" src=3D"https://hs.gigradar.io/hs-fs/hubfs/F=
rame%2034-3.png?width=3D1120&amp;upscale=3Dtrue&amp;name=3DFrame%2034-3.png=
" style=3D"outline:none; text-decoration:none; max-width:100%; font-size:16=
px" width=3D"560" align=3D"middle">
      </td>
    </tr>
  </tbody>
</table></div>
  <table role=3D"presentation" cellpadding=3D"0" cellspacing=3D"0" width=3D=
"100%" class=3D"" style=3D""><tbody><tr><td class=3D"hs_padded" style=3D"fo=
nt-family:Arial, sans-serif; font-size:15px; color:#23496d; word-break:brea=
k-word; padding:10px 20px"><div id=3D"hs_cos_wrapper_module_17550191857382"=
 class=3D"hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" =
style=3D"color: inherit; font-size: inherit; line-height: inherit;" data-hs=
-cos-general-type=3D"widget" data-hs-cos-type=3D"module"><div id=3D"hs_cos_=
wrapper_module_17550191857382_" class=3D"hs_cos_wrapper hs_cos_wrapper_widg=
et hs_cos_wrapper_type_rich_text" style=3D"color: inherit; font-size: inher=
it; line-height: inherit;" data-hs-cos-general-type=3D"widget" data-hs-cos-=
type=3D"rich_text"><p style=3D"line-height:175%"><strong data-stringify-typ=
e=3D"bold">Hi everyone!</strong>&nbsp;=F0=9F=91=8B</p>
<p style=3D"line-height:175%">&nbsp;</p>
<p style=3D"line-height:175%">I know many of you keep asking - how do agenc=
ies actually break through on Upwork and scale beyond just a few contracts?=
</p>
<p style=3D"line-height:175%">Well, this week we=E2=80=99re bringing in som=
eone who=E2=80=99s done exactly that and is ready to share his playbook.&nb=
sp;</p>
<p style=3D"line-height:175%">&nbsp;</p>
<p style=3D"line-height:175%"><strong data-stringify-type=3D"bold">Proven T=
ips to Succeed on Upwork: Real Story from an Agency Owner</strong><br><stro=
ng data-stringify-type=3D"bold">Speaker:</strong>&nbsp;<strong data-stringi=
fy-type=3D"bold"><a href=3D"https://hs.gigradar.io/e3t/Ctc/GF+113/d2hM-B04/=
VXbGfc6jPTQcN4JJLk_jmGQpW1KLHGL5BKpBVN76MZ-P3lYM-W7lCdLW6lZ3lXW5HgXDt7WZkQ3=
N7mY3s_DLwKxW8mVv717yj8Z3W8R0HMz34tn_GW7yk1z739RzTkW1db0Hj7P_jZKW2jydLm3mPL=
YvW6fRHn-2hPgc2W1T28fQ1Zgd8cW1BDsnf16XBwsW3jp4LJ3CMNVHW4qnRBr6F6F4XW7q5dvR5=
RjpfHN70PzRp2QZv-W7GzJ9C8c8Z4rW6m6DTk64ZrvbW6Cw8wG674T4JW8xV5lk3tdJhQN3b615=
jMPFF5W7x8Nfr5Pn5ksW9jgJ2K35gNRXW6b-srL894lYGW1RH9Fd2FgZ0bW2ZSK481Cf3XNf5Mm=
Rkl04" target=3D"_blank" rel=3D"noopener noreferrer" data-member-id=3D"U093=
R4CS371" data-member-label=3D"@Toby Fox-Mason" data-stringify-type=3D"menti=
on" data-stringify-id=3D"U093R4CS371" data-stringify-label=3D"@Toby Fox-Mas=
on" style=3D"color:#00a4bd" data-hs-link-id=3D"0" data-hs-link-id-v2=3D"HXe=
VDnfQ">@Toby Fox-Mason</a></strong><strong data-stringify-type=3D"bold">&nb=
sp;</strong>=E2=80=93 Founder of Ashgrove AI, GigRadar client, and successf=
ul Upwork agency owner.</p>
<p style=3D"line-height:175%">&nbsp;</p>
<p style=3D"line-height:175%"><strong data-stringify-type=3D"bold">=F0=9F=
=8E=AF</strong><strong data-stringify-type=3D"bold">Agenda:</strong><br>=E2=
=80=A2 Challenges he faced on Upwork<br>=E2=80=A2 How he overcame them<br>=
=E2=80=A2 Proven tips that helped him succeed on Upwork&nbsp;</p>
<p style=3D"line-height:175%">&nbsp;</p>
<p style=3D"line-height:175%">=F0=9F=93=86When:&nbsp;<strong data-stringify=
-type=3D"bold"><em data-stringify-type=3D"italic">Aug 28 | 12PM Kyiv | 5PM =
Bali | 5AM EST</em></strong><br>=F0=9F=93=8DWhere: Zoom - <strong data-stri=
ngify-type=3D"bold"><a href=3D"https://hs.gigradar.io/e3t/Ctc/GF+113/d2hM-B=
04/VXbGfc6jPTQcN4JJLk_jmGQpW1KLHGL5BKpBVN76MZ-v3lYM-W6N1vHY6lZ3l3W88D5mF78-=
Vz0W5Rns1Z1zSn2HW324Y1y1dPPQJW4zRCRH7HWZLjW3sWrbm3y0ZR4N3tjrY_fljTGW44rLV98=
_9pK9W2GtHjZ4TjM84W371sSv1mmBdBW7h-KCD3Jd6fXW1WZ3Tx4QTDkDVR6CwC1bS36kW3czWb=
c5PB30wW2Y4Wvv8ZPFGqVlvZ6D731pnyW2QkST274bRcMV2vkLY1jCl3gVRg04q1k2zgJW4gPRD=
83YgcnPW9fdjfJ7jCDKCW4cv0gZ8GTVsPW4tSjYD7x3FL5f1v0c3l04" target=3D"_blank" =
rel=3D"noopener noreferrer" data-stringify-link=3D"https://us06web.zoom.us/=
j/81245073639" data-sk=3D"tooltip_parent" style=3D"color:#00a4bd" data-hs-l=
ink-id=3D"0" data-hs-link-id-v2=3D"02eeWZdU">click here to join</a></strong=
>&nbsp;or&nbsp;<strong data-stringify-type=3D"bold"><a href=3D"https://hs.g=
igradar.io/e3t/Ctc/GF+113/d2hM-B04/VXbGfc6jPTQcN4JJLk_jmGQpW1KLHGL5BKpBVN76=
MZ-v7j1NlW6N2kFb6lZ3lFW1Hm4WJ1_FqZzVbT1rm82zjdSW2sYCk-4dZSmJW67z3_G66BrypVZ=
VngF5LK2BKW1mr--n5t3BdpN8bmL6nm0h4LVnSp-h3WB4s5N8wnHSZhqDt3W3sZvD-3cRcgrW3N=
H2yj9crlC4W7RQkdZ6pFNY2W8fx84G3scZFKW76YVrY2gHghsW8jwbf61vbTwLW99Nc5-6fCqyX=
W29-yKs6-nRL-N7zR0DX91NBPW3F9GwM2yz9QZW1W4BH25HSb-yW3BQm8j8xvLJ1W1-_hQt6x-b=
P_W8dxGzJ5yBp7kW17x7XW3gpTG8W82-JW-1hV-lzW371nmc6SFK4cW7Kjndq73HQn8W9d31dv7=
r7QKJVLJM8x7-K0SmN1C4lVVvcfLLW89dZgR8-v81SW7fG9GQ7G2P_WW4M9bZq2tssJNN6hCmwd=
dsQHCW4ZqsFX64XcSCW48z3Ys6ccqZfW5kBlQ636ndXLVlVCXK73KjvrW8m5Pxc7SZ5F6N3XRrP=
ZT0NLqW97D3Hn1dQJB6W6GDF4x87c6_-N6MwR5VrY2mVW2Ctk2228DnpNW5rmRbN3fS-qMW8N9Q=
y95Cl4zJW1tkSB55LJmP_W2SnRM_3v_D9qW4TxDnb5PxJ8kW7r3PC03wv8vYW2Zy82x3j5L1YW8=
Btpk748vYCDVS5fJN2_4mdHW3B1Tx_4dkftyf55dQfK04" target=3D"_blank" rel=3D"noo=
pener noreferrer" data-stringify-link=3D"https://calendar.google.com/calend=
ar/event?action=3DTEMPLATE&amp;tmeid=3DN3E5YWdjcjM3N2JhcmhxN3NvcWlrMzQ0NTYg=
Y19jNTc4NmQ3MWViNWZmMzliYzFhNGIzMzJjM2MxYjA3OWRiOTVhZmVmZDYxN2MxYTlkZDllNzc=
xOTRiMDdjYWM2QGc&amp;tmsrc=3Dc_c5786d71eb5ff39bc1a4b332c3c1b079db95afefd617=
c1a9dd9e77194b07cac6%40group.calendar.google.com" data-sk=3D"tooltip_parent=
" style=3D"color:#00a4bd" data-hs-link-id=3D"0" data-hs-link-id-v2=3D"5o8Zf=
SLh">add the event</a></strong>&nbsp;to your calendar!&nbsp;</p>
<p style=3D"line-height:175%">&nbsp;</p>
<p style=3D"line-height:175%"><strong data-stringify-type=3D"bold"><a href=
=3D"https://hs.gigradar.io/e3t/Ctc/GF+113/d2hM-B04/VXbGfc6jPTQcN4JJLk_jmGQp=
W1KLHGL5BKpBVN76MZ-v5kvg8W6N1X8z6lZ3k-W7mK84724x3TtW1GQpVq4ZnzCmW22cRhc53VV=
zfW3CTqdN5JpcjYW3TzWn_6R9RJ7N1ptWRtGbK4mW1GbSN461fG8CW5Th_NR3SfKvlW1YYhkx24=
P53RW4ssPml4vmK3bW7Ng35v5M3S9mW60WBCn37TtGpW6Shd806PkS-CW6B6W3Z45J69_VJQgDY=
60f0B4W6RNgR68zh69bN5QsjsQyNbshW7QdGWs6tFYhlVcSNWf3wxNYZW5TLfPV1bkBkmW57YN3=
L2RWS4SW5Zl9dq4Bn9RCW7qbQZL3ymX7qW33Smpd7ZsMPGW213Y0h6m7z2qW7Gpy_V8twYv4N5C=
HwVTGt4jwW5lJRS81zP4lZW3s4s5p7dwG8hW8f1trz27m678W8_v-b-35GymCW3QkgrC1N-kZmW=
2bRHMc50jn43W6hfnWf6ht0xYW33cNSL4Lft4gN8NP4J_MfqDdW72CGCz5h95rlVBsXdD7b2Z_x=
f62P29204" target=3D"_blank" rel=3D"noopener noreferrer" data-stringify-lin=
k=3D"https://calendar.google.com/calendar/u/0?cid=3DY19jNTc4NmQ3MWViNWZmMzl=
iYzFhNGIzMzJjM2MxYjA3OWRiOTVhZmVmZDYxN2MxYTlkZDllNzcxOTRiMDdjYWM2QGdyb3VwLm=
NhbGVuZGFyLmdvb2dsZS5jb20" data-sk=3D"tooltip_parent" style=3D"color:#00a4b=
d" data-hs-link-id=3D"0" data-hs-link-id-v2=3D"KjvwWAZ8">SUBSCRIBE</a></str=
ong><strong data-stringify-type=3D"bold">&nbsp;to our Community Events cale=
ndar to stay updated on upcoming events</strong></p>
<p style=3D"line-height:175%">Don=E2=80=99t miss this chance to learn from =
a real Upwork success story!&nbsp;</p></div></div></td></tr></tbody></table=
>
</div>
<!--[if gte mso 9]></table><![endif]-->
<!--[if (mso)|(IE)]></td><![endif]-->
    <!--[if (mso)|(IE)]></tr></table><![endif]-->
    </div>
  =20
  </div>
  <div id=3D"section-1" class=3D"hse-section hse-section-last" style=3D"pad=
ding-left:10px; padding-right:10px">
   =20
   =20
      <div class=3D"hse-column-container" style=3D"min-width:280px; max-wid=
th:600px; margin:0 auto">
   =20
    <!--[if (mso)|(IE)]>
      <table align=3D"center" style=3D"width:600px;" cellpadding=3D"0" cell=
spacing=3D"0" role=3D"presentation">
      <tr>
    <![endif]-->
    <!--[if (mso)|(IE)]>
  <td valign=3D"top" style=3D"width:600px;">
<![endif]-->
<!--[if gte mso 9]>
  <table role=3D"presentation" width=3D"600" cellpadding=3D"0" cellspacing=
=3D"0" style=3D"width:600px">
<![endif]-->
<div id=3D"column-1-0" class=3D"hse-column hse-size-12">
  <div id=3D"hs_cos_wrapper_module_17562699479711" class=3D"hs_cos_wrapper =
hs_cos_wrapper_widget hs_cos_wrapper_type_module" style=3D"color: inherit; =
font-size: inherit; line-height: inherit;" data-hs-cos-general-type=3D"widg=
et" data-hs-cos-type=3D"module"><table class=3D"hse-image-wrapper" role=3D"=
presentation" width=3D"100%" cellpadding=3D"0" cellspacing=3D"0">
  <tbody>
    <tr>
      <td class=3D"hs_padded" align=3D"center" valign=3D"top" style=3D"font=
-family:Arial, sans-serif; color:#23496d; word-break:break-word; text-align=
:center; padding:10px 20px; font-size:0px">
        <img alt=3D"Event with Tobe Fox-Mason" src=3D"https://hs.gigradar.i=
o/hs-fs/hubfs/Event%20with%20Tobe%20Fox-Mason.png?width=3D1120&amp;upscale=
=3Dtrue&amp;name=3DEvent%20with%20Tobe%20Fox-Mason.png" style=3D"outline:no=
ne; text-decoration:none; max-width:100%; font-size:16px" width=3D"560" ali=
gn=3D"middle">
      </td>
    </tr>
  </tbody>
</table></div>
  <table role=3D"presentation" cellpadding=3D"0" cellspacing=3D"0" width=3D=
"100%" class=3D"" style=3D""><tbody><tr><td class=3D"hs_padded" style=3D"fo=
nt-family:Arial, sans-serif; font-size:15px; color:#23496d; word-break:brea=
k-word; padding:10px 20px"><div id=3D"hs_cos_wrapper_module_17550197213595"=
 class=3D"hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" =
style=3D"color: inherit; font-size: inherit; line-height: inherit;" data-hs=
-cos-general-type=3D"widget" data-hs-cos-type=3D"module"><table align=3D"ce=
nter" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation=
" style=3D"border-collapse:separate!important">
    <tbody><tr>
      <td align=3D"center" valign=3D"middle" bgcolor=3D"#197FC4" style=3D"f=
ont-family:Arial, sans-serif; font-size:15px; color:#23496d; word-break:bre=
ak-word; border-radius:8px; cursor:auto; background-color:#197FC4; mso-padd=
ing-alt:12px 18px">
        <a href=3D"https://hs.gigradar.io/e3t/Ctc/GF+113/d2hM-B04/VXbGfc6jP=
TQcN4JJLk_jmGQpW1KLHGL5BKpBVN76MZ-v5kvg8W6N1X8z6lZ3mrW4fs25g7yPPZ_W1HT1m774=
QvZTN8vdrNwZYP0gW39-3hd1DjJktW1gLhlb23GHzCDbcxqYclS8W939Nrr8yCHNXW76zgfH5ZJ=
fbJW6vgxT83J8kHbV_QPfG8MtwymW7Y_QPL8N2CtnW8Zy1dm24_p_4W3s8RWK5cTqmfW9k8PbS4=
dC89tVMkv5t6GyZ9MW6mJFXQ98zMcWW6fnRQZ3jcwswW1MbW6X1_4d74W13GTBF4cLJ_jN1gr0D=
t39g49VZ0zMM8YZW-HW4qdSP05Vbcm9W28qhL24yzX7NW5dD0tb86PCWXW14vVSD8FZZnHVZ46F=
w6vfnRZW75BRnS388TBBW7GcCKf3wxvVbW7ymFn45k1cgLW545YdH5sgplDW3QyJWP8HJ3dHW7T=
qLB77dqvxQW4y6xpg6hmWMRVjrl2d1ln1HYW6hJMkZ7Br2yhW7zl5Y77HXP6MN8wPTzymQYjZW7=
TWfjs3ShLVqf8YWHtb04" target=3D"_blank" style=3D"color:#00a4bd; font-size:1=
6px; font-family:Arial, sans-serif; Margin:0; text-transform:none; text-dec=
oration:none; padding:12px 18px; display:block" data-hs-link-id=3D"1" data-=
hs-link-id-v2=3D"HQdRH/yd">
          <strong style=3D"color:#ffffff;font-weight:normal;text-decoration=
:none;font-style:normal;">SUBSCRIBE TO THE EVENT CALENDAR</strong>
        </a>
      </td>
    </tr>
  </tbody></table></div></td></tr></tbody></table>
  <table role=3D"presentation" cellpadding=3D"0" cellspacing=3D"0" width=3D=
"100%" class=3D"" style=3D""><tbody><tr><td class=3D"hs_padded" style=3D"fo=
nt-family:Arial, sans-serif; font-size:15px; color:#23496d; word-break:brea=
k-word; padding:10px 20px"><div id=3D"hs_cos_wrapper_module-1-0-0" class=3D=
"hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style=3D"=
color: inherit; font-size: inherit; line-height: inherit;" data-hs-cos-gene=
ral-type=3D"widget" data-hs-cos-type=3D"module"><table role=3D"presentation=
" class=3D"hse-footer hse-secondary" width=3D"100%" cellpadding=3D"0" cells=
pacing=3D"0" style=3D"font-family:Arial, sans-serif; font-size:12px; line-h=
eight:135%; color:#23496d; margin-bottom:0; padding:0">
  <tbody>
    <tr>
      <td align=3D"center" valign=3D"top" style=3D"font-family:Arial, sans-=
serif; font-size:15px; color:#23496d; word-break:break-word; text-align:cen=
ter; margin-bottom:0; line-height:135%; padding:10px 20px">
        <p style=3D"font-family:Arial, sans-serif;font-size:12px;font-weigh=
t:normal;text-decoration:none;font-style:normal;color:#23496d">
          GigRadar, 2810 N Church St PMB 94094, Wilmington, DE 19802-4447, =
US
        </p>
        <p>
          <a data-unsubscribe=3D"true" href=3D"https://hs.gigradar.io/hs/em=
ail-subscriptions/preferences/en/unsubscribe?data=3DW2nXS-N30h-y_W3VHKmP2Rt=
Pm3W3F8n2l2CHzzwW3gqXsc3GS6cpW3_Ym8538ChZWW4tz5ph2r2M_6W34CgMQ1LdVgfW1VgYyD=
3Z_VCnW2KnXmG4pGywQW49xxdS3zkXqpW4pl7JS41QtC_W1VjbBR20T2_WW3N-Rkp41qDYKW32F=
8pZ3yN7JMW25jJtP2CVn_lW2HPQp638BrJhW45BmrY2vLdvxW41XDhD1_mk9-W3F7wfm2vyGBNW=
2PFMy12TPb88W47xdxg1_f2T4W41FhkM38vVTJW2xYKb72Fz_gBW2FVydQ41KTL1W47vBqk4hKf=
_TW3P23F632m8-LW20Z7rl3NWzLNW3yW9Rq3LJzN4W38CCsD2-DGXRW2-v_hN2sMG2_W1LF8543=
Z-zzMW4klrlT3yWZPmW4p9nTL2r8CfyW38mPS12TsNBcW3NLYvn30b7MnW3dwFXR1YW_2WW2RJr=
nK1-YvrCW4mlGhX3R41f5W1Q0R0-34kF95W2r4Q9n3LYTgJW4pl24T4ktzB1W4pHry21BmZF4W3=
_rGD93Kd7TXW36ll502p0rtCW2Kz8Rf23qL0TW4r6C1X2PM3bdW32sBvr1_sMJxW2FS50B2PS_x=
zW2-lg-k4kfTMCW1_pnrt23fz22W1NzygM2PNp4zW2nJqX62YK24S0&amp;utm_source=3Dhs_=
email&amp;utm_medium=3Demail&amp;utm_content=3D377743076&amp;_hsenc=3Dp2ANq=
tz-9j3YQ38Yfcnw_jWlQNUQJTAFHc2vwg-WRqg3qJmSuYEEZoRjucQlMCHNggUDPyNWGXGOvaUJ=
h0Sdvq1t_lh9UZdURQ1QJDGY78mNrQKAByfkeSb7Q&amp;_hsmi=3D377743076" style=3D"f=
ont-family:Helvetica,Arial,sans-serif; font-size:12px; color:#00a4bd; font-=
weight:normal; text-decoration:underline; font-style:normal" data-hs-link-i=
d=3D"0" data-hs-link-id-v2=3D"SFRZzEXk" target=3D"_blank">Unsubscribe</a>
          <a data-unsubscribe=3D"true" href=3D"https://hs.gigradar.io/hs/em=
ail-subscriptions/preferences/en/manage?data=3DW2nXS-N30h-y_W3VHKmP2RtPm3W3=
F8n2l2CHzzwW3gqXsc3GS6cpW3_Ym8538ChZWW4tz5ph2r2M_6W34CgMQ1LdVgfW1VgYyD3Z_VC=
nW2KnXmG4pGywQW49xxdS3zkXqpW4pl7JS41QtC_W1VjbBR20T2_WW3N-Rkp41qDYKW32F8pZ3y=
N7JMW25jJtP2CVn_lW2HPQp638BrJhW45BmrY2vLdvxW41XDhD1_mk9-W3F7wfm2vyGBNW2PFMy=
12TPb88W47xdxg1_f2T4W41FhkM38vVTJW2xYKb72Fz_gBW2FVydQ41KTL1W47vBqk4hKf_TW3P=
23F632m8-LW20Z7rl3NWzLNW3yW9Rq3LJzN4W38CCsD2-DGXRW2-v_hN2sMG2_W1LF8543Z-zzM=
W4klrlT3yWZPmW4p9nTL2r8CfyW38mPS12TsNBcW3NLYvn30b7MnW3dwFXR1YW_2WW2RJrnK1-Y=
vrCW4mlGhX3R41f5W1Q0R0-34kF95W2r4Q9n3LYTgJW4pl24T4ktzB1W4pHry21BmZF4W3_rGD9=
3Kd7TXW36ll502p0rtCW2Kz8Rf23qL0TW4r6C1X2PM3bdW32sBvr1_sMJxW2FS50B2PS_xzW2-l=
g-k4kfTMCW1_pnrt23fz22W1NzygM2PNp4zW2nJqX62YK24S0&amp;utm_source=3Dhs_email=
&amp;utm_medium=3Demail&amp;utm_content=3D377743076&amp;_hsenc=3Dp2ANqtz-9j=
3YQ38Yfcnw_jWlQNUQJTAFHc2vwg-WRqg3qJmSuYEEZoRjucQlMCHNggUDPyNWGXGOvaUJh0Sdv=
q1t_lh9UZdURQ1QJDGY78mNrQKAByfkeSb7Q&amp;_hsmi=3D377743076" style=3D"font-f=
amily:Helvetica,Arial,sans-serif; font-size:12px; color:#00a4bd; font-weigh=
t:normal; text-decoration:underline; font-style:normal" data-hs-link-id=3D"=
0" data-hs-link-id-v2=3D"qjPJqCop" target=3D"_blank">Manage preferences</a>
        </p>
      </td>
    </tr>
  </tbody>
</table></div></td></tr></tbody></table>
</div>
<!--[if gte mso 9]></table><![endif]-->
<!--[if (mso)|(IE)]></td><![endif]-->
    <!--[if (mso)|(IE)]></tr></table><![endif]-->
    </div>
  =20
  </div></div>
          </td>
        </tr>
      </tbody></table>
    </div>
 =20
<img src=3D"https://hs.gigradar.io/e3t/Cto/GF+113/d2hM-B04/VXbGfc6jPTQcN4JJ=
Lk_jmGQpW1KLHGL5BKpBVW76MZLB3DfQGh192" alt=3D"" width=3D"1" height=3D"1" bo=
rder=3D"0" style=3D"display:none!important;min-height:1px!important;width:1=
px!important;border-width:0!important;margin-top:0!important;margin-bottom:=
0!important;margin-right:0!important;margin-left:0!important;padding-top:0!=
important;padding-bottom:0!important;padding-right:0!important;padding-left=
:0!important"></body></html>
------=_Part_10180_618694464.1756271037984--

"""
real_email_3 = """Delivered-To: yevheniia.ilchenko@destilabs.com
Received: by 2002:a05:6838:6527:b2:968:7d74:e7a4 with SMTP id ep7csp263734nkb;
        Wed, 27 Aug 2025 06:58:41 -0700 (PDT)
X-Received: by 2002:a05:690c:892:b0:71f:b944:1035 with SMTP id 00721157ae682-71fdc5313b3mr208357067b3.50.1756303121619;
        Wed, 27 Aug 2025 06:58:41 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1756303121; cv=none;
        d=google.com; s=arc-20240605;
        b=VjVWYcCtvHVg8EUJEyKnWiCnxvqSIpIzUzPxsioPCKoUzNRWokm5m00f6k3pU7yuyG
         VBrutz7q7cIkMGxzJ54QYJ/IhDLeOI8Y7VIrHdvHXiOXV3S+cOIyeLptG85jiX2KOmHs
         qDQRQ0Wp5/eDoBlVAHIU4tt8tWTtBBEdP3ugA0i0cWkqxGnI/wCPFOskEH9G7vEVr0jq
         1Yl3MzjzuCNYm0bSi/5VrLYfA2FiiDPsJDyS3DvX+LeEtKcrS/SZ34M+oPwtII1aJAgS
         3tLwEX4xcA/gTUdKO+NdUvRgpc0YIreTr+dEQLbqwXu8jZJXZALZB4JQ9KJw9mznwXpH
         tpxg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :dkim-signature;
        bh=reM1YmQVnouX6pJE1e6hgRsOv93y+q3c/4YtnLJC0wk=;
        fh=HAMlP18b8NkbM3RF1S047V5u0k2J0lYx0FjjO6Xqv0o=;
        b=gTDzXOstyTPGjN8fAuJ6dO0jbgmCuIzfvZ4PIkP8S+pfWFNTt69zueqRPBQzvCef4N
         jLuJv8RGdcRGtzzG5T1KrUtHEWVuPuiDPG2FNMEY5BZeiL5FXszzSnbQtWnUeHOxq9IC
         mFUTx++OrVoqXGwc15Q8wQh9SNS6lJpSeZXf8BMLHWUibhPUIhzKVc1QLV88GeL7NlEI
         pu9hB8zv4PcDzy8TLGXL9RUMTNBcealEdqGwpw1FZPTmJbGYTTDIg/vodO5CeeSk/nrY
         dHAZQO1wnIrsX2aUO9LJ62G9QHKNwbpE1pJyC7RESRedFXljaES4JL55PmziQRpNDDUe
         w+QA==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b="fN/VPcSz";
       spf=pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=destifor@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=neutral header.i=@destilabs.com
Return-Path: <destifor@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 00721157ae682-71ff1721adbsor80959587b3.3.2025.08.27.06.58.41
        for <yevheniia.ilchenko@destilabs.com>
        (Google Transport Security);
        Wed, 27 Aug 2025 06:58:41 -0700 (PDT)
Received-SPF: pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b="fN/VPcSz";
       spf=pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=destifor@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=neutral header.i=@destilabs.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20230601; t=1756303121; x=1756907921; darn=destilabs.com;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :from:to:cc:subject:date:message-id:reply-to;
        bh=reM1YmQVnouX6pJE1e6hgRsOv93y+q3c/4YtnLJC0wk=;
        b=fN/VPcSzQnnTMr1qzDizA1DVQXnMJ0Cyf0qt3wrLj7HzSVmuJ4BcWvyzkdk5JVRTGm
         likgi+5ruusbRgKK3YVH4N5Pa3XVmXbIoKEiNcJf2SgrSrE9OMcjSJk7r9G7xul0Rcf7
         6dw9PU5eQW8Z6tz12+nH+5K1QKSHh+gGKIE50fizQK2Lfdaf/5Io1rbIb7SfX9CJR6Eg
         p2XGpb69D27HPGwHxYOMQphsZnQedJt3hRnkE1dRTEPQj9SvsJM3sS/FDXC8sksUT+ro
         Ykfeid7E9L8WK1WzoLktc1ozV3kVP56t/AoPPe9PGUZVgBIPIeDqHB/weAcxxORYi/XC
         j/XQ==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1756303121; x=1756907921;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to;
        bh=reM1YmQVnouX6pJE1e6hgRsOv93y+q3c/4YtnLJC0wk=;
        b=C24bgsOShjFBIYI73DAzEHH/0aJ8x3lA5NEER1eCwWOZaeEM1cdnac8RU7ue8sakax
         B9wXQ+HxmOIntvGwRqpwLLV/vjROAxCVT4NlTBQp93jNvB5LycCGPjxQzi98Hu0Xj1rN
         zmerKnr3WWbi1TGyzY/PVYFOqstZHrI46W6Anda0g0ncAobzIX5v3XvLrHD9OVK2jz6w
         BPmb6fusGS8JLjPODc53Kvban7KBhDZG+A47cf4RLo2tTMXqlaOLdyHy/BLa76ISyr66
         jnrnsuP4YiCl50k8pPFfwU0CwJ7dLCGCwf1h8MNjBM3ornckalboE9fkbH10V09yCp4W
         irzw==
X-Gm-Message-State: AOJu0YyjKy5fBE2R1nFHIWD9M2A3vJKnpLuL+UBZcwi3bWIymrdAUFFs
	GgDFOHmIOrW+aQsAcGBTxrWdW12zS15j3KN5xblSLk0WK/6uIDQa1pxGVSp0vsKe2VpXrwXmyEK
	Y2CLcbvmDpox8RIYfEQvZbz4tXLN0DVhm39FY5Fw=
X-Gm-Gg: ASbGncvXlUDmKooMU46NaLcbkuJ39SXKAE7Reco5ZzNSE1Pv0/QXPWDgGb3qgasK5a8
	r9L3TeNjqb3zFIaCrq1AJSRKAjtlXTFL57zguIT/IqAIwdqqD9n56GcYqcDpvorqWwXmDu5ba75
	IExhBUlp0h1MGsd0YjIFEHgcktQT5RCY3BwLQ0le/3te8YmwqCAcHhoSEOq7uKwAIYERcQp09xv
	i1cDpSPyoXOrCWlT/EHkmHHPHMHgs7gaVMyiOiGkOiTAX0ev8IJRxJMY27qrHeiUQGBLa5rOLUb
	MxvBIjw=
X-Google-Smtp-Source: AGHT+IHtQlhDiVAYzM5CoKdGvtGnx+PzF/3xeEsjOZZx4wY3zBRj4a1b77c8HKwvWQrfYZjnKEND3HkgeFMtGN5U+l8=
X-Received: by 2002:a05:6902:2a82:b0:e96:eafc:185 with SMTP id
 3f1490d57ef6-e96eafc0335mr3168027276.7.1756303120424; Wed, 27 Aug 2025
 06:58:40 -0700 (PDT)
MIME-Version: 1.0
References: <4195426f-923a-4d52-b23a-b9d16c2dd983@atl1s07mta1445.xt.local>
In-Reply-To: <4195426f-923a-4d52-b23a-b9d16c2dd983@atl1s07mta1445.xt.local>
From: Mykhaylo Kushnir <destifor@gmail.com>
Date: Wed, 27 Aug 2025 14:58:28 +0100
X-Gm-Features: Ac12FXxtOhsszygOz0vKUKlKD-a3TKoU64WA7EJmi3jJ7GYnxvOYIO0pDBJ4Eq0
Message-ID: <CANPfs47C-Oxijc_U18mMd62mUUW-vCMx_H15DK1CBvnpdQpj3A@mail.gmail.com>
Subject: =?UTF-8?Q?Fwd=3A_The_World_in_Brief=3A_Israel=E2=80=99s_inquiry_into_hos?=
	=?UTF-8?Q?pital_attack?=
To: yevheniia.ilchenko@destilabs.com
Content-Type: multipart/alternative; boundary="0000000000009c66dc063d592f61"

--0000000000009c66dc063d592f61
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

---------- Forwarded message ---------
From: The Economist <noreply@e.economist.com>
Date: Wed, Aug 27, 2025 at 5:51=E2=80=AFAM
Subject: The World in Brief: Israel=E2=80=99s inquiry into hospital attack
To: <destifor@gmail.com>


Also: Europe rallies behind Moldova
 =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C =E2=80=
=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C  =
=E2=80=8C =E2=80=8C
 =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C
 =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C =E2=80=
=8C  =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C=
 =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C
 =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C   =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=
=8C  =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =
=E2=80=8C =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C
 =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C  =E2=80=8C =E2=80=8C   =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=
=8C  =E2=80=8C =E2=80=8C
[image: The Economist]
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb2364c2eb3229484a97ed5=
7ee141b03ab3550f6da9c50833844a14ae2989dcf5c0a53f1d803555b81ab3a339ad867f58d=
9169bc223c2eff577>

Read in browser
<https://view.e.economist.com/?qs=3Dded59c1a738a945e20d5b04c45dad825c2c2710=
5bd2a473e8dc5ed349b6ecebe4a44c611ed8742f6906a6a5b1c179f80c5f622673cd1d6f9f3=
569f495dfbdeeadab589a427baafbb400e6a82bae412ec>

August 27th 2025
[image: Catch up quickly on the global stories that matter]

SUBSCRIBER ONLY
The World in Brief

Catch up quickly on the global stories that matter
------------------------------
<https://click.e.economist.com/u/?qs=3D6eaea0acd4a831365e2b31cfaa4a15df30c4=
7ec8cee4b02908eb9b587de4e614275de25581c7c0bef1892204862f0f15d5f164a2b68c0e1=
5f97076adb0140acf>
[image:
timer] [image: trk_px]

<https://click.e.economist.com/?qs=3D6eaea0acd4a831367f75b0424d7a412a1eac63=
ecd8662d06e009d31c007937a0e55ae2e0dbe983a877922be14cfe63f5f31061f6c57c169f>
PHOTO: GETTY IMAGES
<https://click.e.economist.com/?qs=3D6eaea0acd4a831363b6035d72a0348a52c7bcc=
ed17a09fc0a263e670ebd297a5015d2cf1dd8930643e2802a5764188a881718e640818d263>

*Joshua Spencer
<https://click.e.economist.com/?qs=3D6eaea0acd4a831363b6035d72a0348a52c7bcc=
ed17a09fc0a263e670ebd297a5015d2cf1dd8930643e2802a5764188a881718e640818d263>=
*
News editor
Good morning. In today=E2=80=99s edition: Israel releases inquiry into hosp=
ital
attack, Europe rallies behind Moldova and the battle for surfing=E2=80=99s =
crown
begins.

Elsewhere in *The Economist*: reconsidering your holiday to America? We
turn to the data to find out whether the country is really losing its
appeal among foreign tourists
<https://click.e.economist.com/?qs=3D6eaea0acd4a83136bbf3f6e6775064b7066043=
2e453f1ffcdf28bcea66888b25b6a8d44f2c97793d2a6e86dfda1453ece58c8e6089c7bac1>
.
*Today=E2=80=99s top stories*

An =E2=80=9Cinitial inquiry=E2=80=9D released by the *Israel Defence Forces=
 *claimed troops
attacked Nasser hospital in southern *Gaza* on Monday after identifying a
=E2=80=9Ccamera that was positioned by Hamas=E2=80=9D. At least 20 people w=
ere killed,
including
five journalists
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb23f624642bc56200228c65a=
8399637f8b1e585e529a35a41e83c016a761816b4ff6c65e92d3bf464ff115d9aa76ef7ab2>=
.
On Tuesday the UN said that there =E2=80=9Cneeds to be justice=E2=80=9D for=
 the attack.
Meanwhile protesters in Israel called for the release of hostages and an
end to the war.
*Donald Trump* said he had several =E2=80=9Cgood people=E2=80=9D in mind to=
 replace *Lisa
Cook *on the Federal Reserve=E2=80=99s board, but that he would abide by an=
y court
decision that left her in her job. Ms Cook=E2=80=99s lawyers indicated that=
 she
would sue to block Mr Trump=E2=80=99s =E2=80=9Cillegal=E2=80=9D attempt to =
sack her
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb20967b40c7f2dfb7eedfe58=
6f481373e7ff1f74be581853ca02f4546c5dedc40c64746124fbf5e86d6049db8901df3aa0>=
.
She is alleged to have made false statements on her mortgage.
*SpaceX=E2=80=99s Starship, *the world=E2=80=99s largest and most powerful =
rocket, made it
up to space and back down to Earth during its tenth test flight. The
largely successful mission is a boost for Elon Musk, SpaceX=E2=80=99s boss.=
 The
previous three tests of the Starship launch system
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb2875e5a65076082a5b132ca=
338b460600278afefdb3a29baf4baa069ed5d5dd92668a03caedfb9a0c61a20eeae2c7e454>
all failed to meet their intended goals. One blew up on the ground in June.
Officials in *Pakistan* warned that the Punjab region faces =E2=80=9Cvery h=
igh to
exceptionally high=E2=80=9D danger of flooding. Earlier this week India ale=
rted its
neighbour about possible cross-border flooding as it planned to release
water from overflowing dams. It was the first public contact between the
countries since a four-day conflict
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb20a10f4f272afba02fc117e=
780ddc4a46404f45c248377eb94d6c9712794b8f8747fe7099b347a184c35e4ac29ad4d7e2>
in May. Weeks of heavy rain have battered the region. Rescuers have
evacuated more than 150,000 people.
*Howard Lutnick* hinted that the Trump administration was considering
buying stakes in *defence companies*. Speaking to CNBC, the commerce
secretary called Lockheed Martin, an arms manufacturer, =E2=80=9Cbasically =
an arm
of the US government=E2=80=9D and said that defence procurement had =E2=80=
=9Cbeen a
giveaway=E2=80=9D. Lockheed=E2=80=99s shares jumped on the news. Last week =
America=E2=80=99s
government took a 10% stake in Intel
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb254da71222c6077acb02748=
46a8270aae9a6c18f118bcaf57bbab0c580bfe7ce032a08d086ef474b08d7c5962e9ce8963>=
,
an ailing chipmaker.
*Trump Media and Technology Group*, the Trump family=E2=80=99s media firm, =
said it
would create a =E2=80=9Cdigital asset treasury company=E2=80=9D with Crypto=
.com, a currency
exchange, and Yorkville Acquisition, a blank-cheque firm. The new company
plans to raise $6.4bn to buy CRO, the digital token native to Crypto.com.
America=E2=80=99s president favours crypto-friendly laws
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb210aa42cf899a2918e747ac=
101efdf0740c690edb4d63d4aec5a0183760109f0ea31cfdd5dda9385041462d07f7cf3f20>=
;
his family has gradually expanded its digital-asset portfolio.
Abdulkadir Uraloglu, *Turkey=E2=80=99s* transport minister, was fined aroun=
d 9,000
lira ($220) after sharing a video of himself on social-media driving at
225kph, more than 80kph above the speed limit. The clip showed him
listening to speeches by Recep Tayyip Erdogan
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb267d177a6fe93f91fce9af5=
73ec83bb4a580ee492f2c00f9b98e5bc43a50db182a8b8fc101712ad11627541ceb6f4f001>=
,
Turkey=E2=80=99s president, and Turkish folk music. He added the hashtag
#TurkeyAccelerates. He later apologised for speeding =E2=80=9Cunintentional=
ly=E2=80=9D.
*Donald Trump=E2=80=99s presidency has brought exceptional changes to Ameri=
can
politics. Read The US in brief
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb2de354c58b7dbca1ba06aea=
a6cf59334eec32017ec612f7b55bc94452983d9d3317bb12e3eaeb69000a8fc221b99ec01b>=
,
a daily update of the domestic political stories that matter.*

------------------------------
*Figure of the day:* 54,000, the number of exit bans issued by Chinese
courts last year, more than double the 24,000 in 2022. Read the full story
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb2afe14c0ec5aa0cbc85d274=
2892362f184a0acfd06c5e3b81f2f9adfe5a7045b40b869029da237fa0540bd21b0ac45ad5>
.

------------------------------
<https://click.e.economist.com/u/?qs=3D6eaea0acd4a8313643ffdffb00d1835012f2=
9530ce0869fb231712682acea2ff071a1b6a308653279a8b3efde60ee8dacf30f1d577b6310=
6233d646f3c2b3dfb>
[image:
timer] [image: trk_px]
*The day ahead*
*Donald Trump=E2=80=99s war on the Fed*
[image: Federal Reserve Governor Lisa Cook attends the Federal Reserve Bank
of Kansas City's 2025 Jackson Hole economic symposium,]
REUTERS
On Sunday Donald Trump declared that he wanted to fire Lisa Cook
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb20967b40c7f2dfb7eedfe58=
6f481373e7ff1f74be581853ca02f4546c5dedc40c64746124fbf5e86d6049db8901df3aa0>=
,
a governor of the Federal Reserve, over claims she had lied on mortgage
applications. Ms Cook has not been charged with any crime, although the
Department of Justice says it plans to open an investigation. She has
refused to resign, calling her would-be sacking unlawful.

Pressure on the Fed has been rising for months. Mr Trump wants the central
bank to cut interest rates faster=E2=80=94a tall order when tariffs have ke=
pt
inflation above its 2% target. He has mused about firing Jerome Powell, its
chairman, citing a costly renovation of the Fed=E2=80=99s offices in Washin=
gton as
a potential pretext. But the president=E2=80=99s power to dismiss top Fed o=
fficials
is legally uncertain and, so far, untested. A Supreme Court ruling from
1935 prevents the president from firing governors =E2=80=9Cwithout cause=E2=
=80=9D. But recent
rulings
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb238f9abd047450f861fb11f=
40a09ae2a92e384f4d8395f67ac11b8baa8b988e5b9590d689825cf40f34d94b7a0844cb9b>
by the justices have weakened that precedent. What happens next will be up
to the courts.

*China clouds Nvidia=E2=80=99s horizon*
[image: Co-founder, president and CEO of Nvidia Corporation, Jensen Huang,
presents NVIDIA Blackwell GPU as he delivers his keynote speech ahead of
the COMPUTEX trade show, in Taipei, Taiwan.]
SHUTTERSTOCK
Nvidia, an American chipmaker, is expected to issue a strong earnings
report on Wednesday. Booming demand for artificial-intelligence kit among
America=E2=80=99s tech giants continues to drive revenue, especially as shi=
pments
of its new Blackwell chips increase. The world=E2=80=99s most valuable comp=
any has
unofficially guided that second-quarter revenues will be $45bn, but
analysts expect it to beat that by at least $1bn.

Its third-quarter outlook could rise to $54bn or more. Whether it can go
higher will depend on geopolitics. Earlier this month, the Trump
administration granted Nvidia permission to resume sales to China
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb2664d1f38bee0cb1c8086d9=
69ac050afdf51504ac773571430881b0a9072c43c35d998e32fbd5a9e5ff640dc6194d6d33>
of its H 20 chips, which Nvidia devised to comply with American export
controls. But the Chinese government warned that the chips were a security
risk and discouraged customers from buying them. Nvidia is now lobbying
Donald Trump to allow sales of modified Blackwell chips to China. If it
succeeds, revenues could climb. But Mr Trump wants America=E2=80=99s govern=
ment to
receive a cut of such sales=E2=80=94one that would dent Nvidia=E2=80=99s pr=
ofits.

[image: Chart image]
*Europe rallies behind Moldova*
[image: President of Moldova Maia Sandu.]
AP
Moldova declared independence from the Soviet Union on August 27th 1991. On
Wednesday France=E2=80=99s president, Germany=E2=80=99s chancellor and Pola=
nd=E2=80=99s prime
minister will visit to help Maia Sandu, Moldova=E2=80=99s president, preven=
t the
country from falling back into Russia=E2=80=99s orbit
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb244bdcb25c6f3b1ea515640=
66cd5c9b5009d00477baee561f5a398c91c7b7d1f1b7d86e829af6771a8e670f45dba0f744>=
.
Emmanuel Macron, Friedrich Merz and Donald Tusk see Moldova (home to 2.4m
people, including Russian and Romanian speakers, and wedged between Ukraine
and Romania) as vital to European security.

Ms Sandu, an anti-corruption campaigner and stalwart ally of Ukraine, has
been guiding the country through its candidacy for membership of the
European Union. She was re-elected last year despite facing disinformation
and vote-buying, allegedly orchestrated
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb2a82f020f978ee7371a8f26=
eebeee802accb3c0a6932ae0ff4a15ac02b2773fb188f3dbeacb58afe7bd9075c5c1cd59b6>
by Russia and its allies in Moldova. Her party is likely to lose its
majority in a parliamentary election on September 28th. France is
particularly concerned. Its cyber-agency works closely with Moldova=E2=80=
=99s, and
Mr Macron has his own experience with Russian meddling. European leaders
hope that the high-profile visit helps Ms Sandu shore up support.

*CrowdStrike rides the AI wave*
[image: The CrowdStrike logo is seen displayed on a smartphone screen.]
GETTY IMAGES
On Wednesday CrowdStrike reports quarterly earnings. The outlook for the
American cyber-security giant is strong, reflecting a boom across the
sector. Global spending on cyber-security is expected to reach $213bn this
year, up from $193bn in 2024. The NASDAQ CTA Cyber-security Index, which
tracks big firms that provide digital defences, has jumped by more than 20%
in the past 12 months. CrowdStrike=E2=80=99s stock is up by more than 55% o=
ver the
same period.

Artificial intelligence is the big driver. Smarter models are improving
detection of malware, vulnerabilities and suspicious network behaviour.
Some firms, including CrowdStrike, are also investing in =E2=80=9Cagentic=
=E2=80=9D systems
that respond to threats automatically. But the AI arms race cuts both ways.
Criminals are using the technology
<https://click.e.economist.com/?qs=3D4c03d7505d8b6cb221c391beff7da441d879e9=
76d8b1db67175de3fedcd1a2a085fbc3ecaaf3f74dd08e330a4c64a4ba0d89d0c7040787c5>
to generate stealthier malware and more convincing phishing lures. In April
the FBI reported that America=E2=80=99s losses to internet crime in 2024 ha=
d surged
to $17bn, up by a third on the previous year.

*The battle for surfing=E2=80=99s crown begins*
[image: Molly Picklum of Australia surfs in a big wave - Teahupoo, Tahiti,
French Polynesia.]
GETTY IMAGES
On Wednesday the World Surf League opens its nine-day window to crown its
champions for 2025. Surf competitions depend on conditions, which is why
the league gives itself more than a week to run the finals. This year they
are held at Cloudbreak, a remote reef break off the coast of Fiji. Its
waves are known for their speed and size, making them some of the most
difficult=E2=80=94and spectacular=E2=80=94in the world to surf.

The format rewards consistency. Since January, surfers have competed at 11
locations worldwide. The top five men and women now face off in Fiji in
head-to-head heats: fifth versus fourth, the winner against third, and so
on, until a challenger meets the top seed.

Australia=E2=80=99s Molly Picklum leads the women=E2=80=99s field, which al=
so includes two
American former champions: Caroline Marks and Caitlin Simmers. Brazil=E2=80=
=99s
Yago Dora tops the men=E2=80=99s rankings. The sole former champion in the =
men=E2=80=99s
draw is the fifth seed, Italo Ferreira, but he will need a spectacular run
to take the title.

*Daily quiz*
THE ECONOMIST

*Wednesday: *Which Bobby Goldsboro song was the best-selling record
worldwide in 1968?

*Tuesday: *What type of people did Karl Marx and Friedrich Engels call upon
to =E2=80=9Cunite=E2=80=9D in the Communist Manifesto?

We will serve you a new question each day this week. On Friday your
challenge is to give us all five answers and, as important, tell us the
connecting theme. Email your responses (and include mention of your home
city and country) by 1700 BST on Friday to QuizEspresso@economist.com.
We=E2=80=99ll pick randomly from those with the right answers and crown thr=
ee
winners on Saturday.



Words are but the vague shadows of the volumes we mean.
------------------------------
*Theodore Dreiser*


We=E2=80=99d value your feedback on the World in Brief newsletter. You can =
share
your thoughts and suggestions with us directly here:
worldinbrief@economist.com.

This email has been sent to: destifor@gmail.com. If you'd like to update
your details please click here
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb2a80a0cf568640ac2f7f6=
93fdda238e9ff04c94eed854b1670ca90f78826a6f3a2e3d4ee8c05346a53b7d78f3e630142=
e3e74e1e5fb650ec0>.
Replies to this email will not reach us. If you don't want to receive these
updates anymore, please unsubscribe here
<https://myaccount.economist.com/s/preferences?contactId=3D0033z000035LcCMA=
A0&newslettercode=3Despresso>.


Join the conversation
[image: LinkedIn]
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb2e3368f8650aaf0524945=
fb3c8862b319f0a06fc73243f0c6e097160203960c58404e71c9715a8b3b8ac0d7827c2a93d=
13d07a874716fff1a>
[image:
Facebook]
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb2ebd6469d11ec27ca043c=
0bbb053f7186bad3db3a81f9e8dbd64ddc6bf7b10a7b9d7825fcf34311266b018a3a8f767fe=
3a4e507aff1e5c02b>
[image:
X]
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb29aac58457e6b20b38adf=
aca1ae7831d94fcf16a140994ab94148957fbfdad4ded8b77fe0e953e35ad3e80b232dea7d7=
d0e6af37b530039a6>
[image:
Instagram]
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb277d5af3f46a05283982e=
b6a5c6c6d16d8ebeb5dd463f5b61331d86d4760df57d20a0cfb96131ef8bd9d3590a1fe0546=
039d008b38ab6526b>
[image:
32]
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb2ef3aec0587aa41bb9ab9=
da4984c10c8e350c4f51d87d045cf9fa72a9a65181ae0348a11e48a77ad321f1077fe656fc9=
f9187a98bbda3a1d3>
[image:
TikTok]
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb294cb802a58dc061638b0=
08cc49333a3323b5e67a433e1e32aa5a7a9cb4fbd7544102741c1554235a187ad5a15249dea=
f0fe9e0e1b39f1e88>
[image:
Youtube]
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb251342262b59d204f7ccc=
cbb9e9c8221391a4b4ec76ff2e940220c048002907bb0e6e9ebb814191db149d863edab5b08=
f80d6c833e0463132>

Advertising Info
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb28a049696d793d722e715=
4cb5e01490ba2afbe6b168b889fd0d9a589bf21439d4777a34bf1c5beda28f3a2cc5bb74838=
4>

Terms & Conditions
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb2dcebf37a136f265523ca=
02d10714c429e67810856ea03627ade8f8f0b60d5f8e6dbcab4162e8e2f9536c6f366f64cc3=
5808387836f64997d>

Help
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb27361786a4e713230c0c0=
2b4c0c569c7abf4ead76a9db7e7c40fa54a9f9ac3eef030d5a6a43f6e82c42fcced72ebc421=
06c5e2ff41edce584>

Privacy Policy
<https://click.e.economist.com/u/?qs=3D4c03d7505d8b6cb2bac49db1f48f0ba62257=
cafcdff891644817f7716edb0a88b794d05883f1b499f84a173f43aa0522fae28d96104f83f=
b49eaa13f1085b404>

Copyright =C2=A9 The Economist Newspaper Limited 2025. All rights reserved.

Registered in England and Wales. No.236383


Registered office: The Adelphi, 1=E2=80=9311 John Adam Street, London, WC2N=
 6HT
This email was sent to: destifor@gmail.com

This email was sent by: The Economist Newspaper Ltd., The Adelphi, 1-11
John Adam Street, London, London, WC2N 6HT, GB

--0000000000009c66dc063d592f61
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr"><br><br><div class=3D"gmail_quote gmail_quote_container"><=
div dir=3D"ltr" class=3D"gmail_attr">---------- Forwarded message ---------=
<br>From: <strong class=3D"gmail_sendername" dir=3D"auto">The Economist</st=
rong> <span dir=3D"auto">&lt;<a href=3D"mailto:noreply@e.economist.com">nor=
eply@e.economist.com</a>&gt;</span><br>Date: Wed, Aug 27, 2025 at 5:51=E2=
=80=AFAM<br>Subject: The World in Brief: Israel=E2=80=99s inquiry into hosp=
ital attack<br>To:  &lt;<a href=3D"mailto:destifor@gmail.com">destifor@gmai=
l.com</a>&gt;<br></div><br><br><div class=3D"msg2475453623025163034">











































































































































































































































































































































































































































































































































































































































<u></u>

   =20
     =20
   =20
   =20
   =20
   =20
   =20
   =20
   =20
   =20
   =20
   =20
   =20
   =20
   =20
   =20
 =20
   =20
<div id=3D"m_-8463748081042192912body" bgcolor=3D"#f2f2f2" style=3D"width:1=
00%!important;margin:0 auto;padding:0;background-color:#f2f2f2">
<div style=3D"font-size:1px;display:none!important">Also: Europe rallies be=
hind Moldova</div>
    <div style=3D"display:none">
      <img src=3D"https://click.e.economist.com/open.aspx?ffcb10-fea0167175=
67047f72-fe1d16717c630d7f711c78-fe8d13727c650c7976-ff3615707661-fe2c1674756=
60c7a741d72-ff031576756401&amp;d=3D70249&amp;bmt=3D0" width=3D"1" height=3D=
"1" alt=3D"">
    </div>
      =20
    <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"prese=
ntation" style=3D"min-width:100%"><tbody><tr><td>   =20
<div style=3D"max-height:0;overflow:hidden" aria-hidden=3D"true">=C2=A0=E2=
=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=
=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=C2=
=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
  =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0  =C2=A0=E2=80=8C=C2=A0=E2=80=
=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=C2=A0=E2=
=80=8C=C2=A0=E2=80=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=
=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=
=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0  =C2=
=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=
=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=
=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=20
 =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0  =C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=C2=A0=E2=80=8C=
=C2=A0=E2=80=8C=C2=A0  =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0
    </div>
</td></tr></tbody></table>
   =20
   =20
   =20
    <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"prese=
ntation" style=3D"min-width:100%"><tbody><tr><td></td></tr></tbody></table>
   =20
   =20
   =20
   =20
   =20


   =20

   =20
   =20
 =20
   =20
    <div style=3D"max-height:0;overflow:hidden" aria-hidden=3D"true">
    </div>
   =20
   =20
    <center style=3D"width:100%!important;height:100%!important;table-layou=
t:fixed!important;background-color:#f2f2f2">
     =20
      <div role=3D"document" style=3D"max-width:600px;margin:0 auto;backgro=
und-color:#ffffff">
       =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td>    <table width=3D"10=
0%" align=3D"center" bgcolor=3D"#ffffff" cellspacing=3D"0" cellpadding=3D"0=
" border=3D"0" role=3D"presentation" style=3D"max-width:600px">
          <tbody><tr>
            <td class=3D"m_-8463748081042192912pt24-pb32" valign=3D"top" st=
yle=3D"padding:16px 16px 24px 16px">
              <table width=3D"100%" cellspacing=3D"0" cellpadding=3D"0" bor=
der=3D"0" role=3D"presentation">
                <tbody><tr>
                  <td width=3D"128" align=3D"left" valign=3D"middle" style=
=3D"vertical-align:middle;padding:0 16px 0 0">
                    <a href=3D"https://click.e.economist.com/u/?qs=3D4c03d7=
505d8b6cb2364c2eb3229484a97ed57ee141b03ab3550f6da9c50833844a14ae2989dcf5c0a=
53f1d803555b81ab3a339ad867f58d9169bc223c2eff577" target=3D"_blank">
                      <img src=3D"https://image.e.economist.com/lib/fe8d137=
27c650c7976/m/1/d2979654-fae4-451b-bdca-c79bb5522f6b.png" width=3D"128" hei=
ght=3D"64" alt=3D"The Economist" border=3D"0" style=3D"display:block;border=
:none">
                    </a>
                  </td>
                  <td class=3D"m_-8463748081042192912econsans" valign=3D"mi=
ddle" style=3D"vertical-align:middle;font-family:EconomistSansLF,system-ui,=
Segoe UI,Helvetica,Arial,sans-serif;font-size:14px;color:#121212;line-heigh=
t:25px;text-align:right;border-top:1px solid #d7d7d7;border-bottom:1px soli=
d #d7d7d7">
                    <p style=3D"margin:0">
                      <a href=3D"https://view.e.economist.com/?qs=3Dded59c1=
a738a945e20d5b04c45dad825c2c27105bd2a473e8dc5ed349b6ecebe4a44c611ed8742f690=
6a6a5b1c179f80c5f622673cd1d6f9f3569f495dfbdeeadab589a427baafbb400e6a82bae41=
2ec" style=3D"color:#121212;text-decoration:none" target=3D"_blank">Read in=
 browser </a>
                    </p>
                  </td>
                </tr>
              </tbody></table>
            </td>
          </tr>
        </tbody></table></td></tr></tbody></table>   =20
       =20
       =20
        <table role=3D"presentation" style=3D"max-width:600px" width=3D"100=
%" cellspacing=3D"0" cellpadding=3D"0" border=3D"0" bgcolor=3D"#ffffff" ali=
gn=3D"center">
          <tbody><tr>
            <td style=3D"padding:0 16px 16px 16px" valign=3D"top">
              <table role=3D"presentation" width=3D"100%" cellspacing=3D"0"=
 cellpadding=3D"0" border=3D"0">
                <tbody><tr>
                  <td class=3D"m_-8463748081042192912econsans" style=3D"pad=
ding:4px 0 0 0;font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Ari=
al,sans-serif;font-size:11px;color:#121212;line-height:19px;text-align:left=
;text-transform:uppercase;border-top:1px solid #121212" valign=3D"top">
                    <p style=3D"margin:0">
                      August 27th 2025</p>
                  </td>
                </tr>
              </tbody></table>
            </td>
          </tr>
        </tbody></table>
       =20
       =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center=
" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=
=3D"presentation" style=3D"max-width:600px" width=3D"100%">
  <tbody><tr>
    <td align=3D"center" style=3D"font-size:0;padding:0 0 20px 0" valign=3D=
"top">
     =20
      <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bl=
ock;width:100%;min-width:100%;max-width:120px;letter-spacing:normal;vertica=
l-align:top">
        <table align=3D"right" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912fluid" role=3D"presentation" width=3D=
"100%">
          <tbody><tr>
            <td align=3D"center" style=3D"padding:1px 0px 1px 0px" valign=
=3D"middle">
              <img alt=3D"Catch up quickly on the global stories that matte=
r" height=3D"80" src=3D"https://image.e.economist.com/lib/fe8d13727c650c797=
6/m/5/90355b7b-c14d-459f-8cfa-a4e414e41182.png" style=3D"display:block;padd=
ing:0px;height:80px;width:80px;text-align:center;border:0px none transparen=
t" width=3D"80">
            </td>
          </tr>
        </tbody></table>
      </div>
     =20
      <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bl=
ock;width:100%;min-width:100%;max-width:480px;vertical-align:top">
        <table align=3D"left" border=3D"0" cellpadding=3D"0" cellspacing=3D=
"0" role=3D"presentation" width=3D"100%">
         =20
          <tbody><tr>
            <td class=3D"m_-8463748081042192912pt0-12 m_-846374808104219291=
2pr16" height=3D"15px" style=3D"vertical-align:middle;padding:0px 16px 0px =
0px" valign=3D"middle">
              <p class=3D"m_-8463748081042192912txtl m_-8463748081042192912=
econsans" style=3D"margin:0px;font-family:EconomistSansLF,system-ui,Segoe U=
I,Helvetica,Arial,sans-serif;font-size:11px;color:#e3120b;line-height:15px;=
letter-spacing:normal;font-weight:500!important;text-align:center">
                <a rel=3D"noopener" style=3D"color:#e3120b;text-decoration:=
none" title=3D"">SUBSCRIBER ONLY</a>
              </p>
            </td>
          </tr>
         =20
          <tr>
            <td class=3D"m_-8463748081042192912pr16" height=3D"44" style=3D=
"vertical-align:middle;padding:0px 16px 0px 0px" valign=3D"middle">
              <h1 class=3D"m_-8463748081042192912txtl m_-846374808104219291=
2txt36 m_-8463748081042192912serifLF" style=3D"margin:0px 0px;font-family:E=
conomistSerifLF,Georgia,TimesNewRoman,Times New Roman,Times,serif;font-size=
:32px;color:rgb(18,18,18);line-height:38px;letter-spacing:normal;font-weigh=
t:500!important;text-align:center">
                The World in Brief</h1>
            </td>
          </tr>
          <tr>
            <td class=3D"m_-8463748081042192912pr16" height=3D"28" style=3D=
"vertical-align:middle;padding:0px 16px 0px 0px" valign=3D"middle">
              <p class=3D"m_-8463748081042192912txtl" style=3D"margin:0px;f=
ont-size:20px;color:rgb(18,18,18);line-height:1.4;font-weight:400!important=
;text-align:center">
                Catch up quickly on the global stories that matter</p>
            </td>
          </tr>
        </tbody></table>
      </div>
     =20
    </td>
  </tr>
</tbody></table>

<table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" =
cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"=
100%">
  <tbody><tr>
    <td style=3D"padding:0 8px 0px 8px" valign=3D"top">
      <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" width=3D"100%">
        <tbody><tr>
          <td align=3D"center" style=3D"padding:0 8px 8px 8px" valign=3D"to=
p">
            <hr style=3D"width:100%;max-width:568px;height:1px;margin:0;bac=
kground-color:#d7d7d7;color:#d7d7d7;border-width:0">
          </td>
        </tr>
      </tbody></table>
    </td>
  </tr>
</tbody></table>

</td></tr></tbody></table>
       =20
       =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td>
<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td>
<table width=3D"100%" align=3D"center" bgcolor=3D"#ffffff" cellspacing=3D"0=
" cellpadding=3D"0" border=3D"0" role=3D"presentation" style=3D"max-width:6=
00px">
    <tbody><tr>
     <td style=3D"padding:0 0px 0 0px" valign=3D"top" align=3D"center">
        <a href=3D"https://click.e.economist.com/u/?qs=3D6eaea0acd4a831365e=
2b31cfaa4a15df30c47ec8cee4b02908eb9b587de4e614275de25581c7c0bef1892204862f0=
f15d5f164a2b68c0e15f97076adb0140acf" target=3D"_blank">
          <img style=3D"display:block;width:100%;max-width:600px;height:aut=
o;border:none;padding:0px;text-align:center" src=3D"https://pas.economist.c=
om/view/2/39681/4d3a2e8304eb98061411f3051e4142e5/2103027?ad_region=3DEurope=
&amp;ad_country=3DUkraine&amp;send_date=3D26/08/2025" width=3D"600">
        </a>
        <img width=3D"1" height=3D"1" style=3D"display:none" alt=3D"timer" =
src=3D"https://pas.economist.com/t/2/39681/0033z000035LcCMAA0/2103027?pid=
=3D1&amp;ad_region=3DEurope&amp;ad_country=3DUkraine&amp;send_date=3D26/08/=
2025">
        <img width=3D"1" height=3D"1" style=3D"display:none" alt=3D"trk_px"=
 src=3D"https://pas.economist.com/extt/2/39681/0033z000035LcCMAA0/2103027?p=
id=3D1&amp;ad_region=3DEurope&amp;ad_country=3DUkraine&amp;send_date=3D26/0=
8/2025">
      </td>
    </tr>
  </tbody></table>
     =20
</td></tr></tbody></table></td></tr></tbody></table><table cellpadding=3D"0=
" cellspacing=3D"0" width=3D"100%" role=3D"presentation" style=3D"min-width=
:100%"><tbody><tr><td><table align=3D"center" bgcolor=3D"#ffffff" border=3D=
"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-=
width:600px" width=3D"100%">
=09
		<tbody><tr>
			<td style=3D"padding:0 16px 8px 16px" valign=3D"top">
				=C2=A0<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"p=
resentation" width=3D"100%">
				=09
						<tbody><tr>
							<td align=3D"center" style=3D"padding:0 0 24px 0;border-bottom:0px s=
olid #d7d7d7" valign=3D"top">
								<img alt=3D"" src=3D"https://image.e.economist.com/lib/fe8d13727c65=
0c7976/m/1/8035ff37-6758-4ed2-ae4b-1673827ea6c0.jpg" style=3D"display:block=
;width:100%;max-width:568px;height:auto;padding:0px;text-align:center;borde=
r:0px" width=3D"568"><a href=3D"https://click.e.economist.com/?qs=3D6eaea0a=
cd4a831367f75b0424d7a412a1eac63ecd8662d06e009d31c007937a0e55ae2e0dbe983a877=
922be14cfe63f5f31061f6c57c169f" target=3D"_blank"> </a></td></tr></tbody></=
table></td></tr></tbody></table></td></tr></tbody></table><table cellpaddin=
g=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentation" style=3D"min=
-width:100%"><tbody><tr><td><table align=3D"center" bgcolor=3D"#ffffff" bor=
der=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" style=
=3D"max-width:600px" width=3D"100%">
=09
		<tbody><tr>
			<td style=3D"padding:0 16px 0 16px" valign=3D"top">
				<table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D=
"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
				=09
						<tbody><tr>
							<td style=3D"padding:0 0 12px 0" valign=3D"top">
								<span style=3D"color:rgb(51,51,51);font-family:EconSansOS,EconSansO=
SSec,-apple-system,BlinkMacSystemFont,&quot;Segoe UI&quot;,Helvetica,Arial,=
sans-serif;font-size:11.2373px;font-style:normal;font-variant-ligatures:nor=
mal;font-variant-caps:normal;font-weight:400;letter-spacing:0.3px;text-alig=
n:start;text-indent:0px;text-transform:uppercase;white-space:normal;word-sp=
acing:0px;text-decoration-style:initial;text-decoration-color:initial;displ=
ay:inline!important;float:none">PHOTO: GETTY IMAGES</span></td></tr></tbody=
></table></td></tr></tbody></table></td></tr></tbody></table>
       =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center=
" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=
=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=09
		<tbody><tr>
			<td align=3D"left" style=3D"padding:0 16px 16px 16px" valign=3D"top">
				<table align=3D"left" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" =
role=3D"presentation">
				=09
						<tbody><tr>
							<td style=3D"vertical-align:middle;padding:0 16px 0 0" valign=3D"mid=
dle" width=3D"67">
								<a href=3D"https://click.e.economist.com/?qs=3D6eaea0acd4a831363b60=
35d72a0348a52c7bcced17a09fc0a263e670ebd297a5015d2cf1dd8930643e2802a5764188a=
881718e640818d263" title=3D"" target=3D"_blank"><img alt=3D"" src=3D"https:=
//image.e.economist.com/lib/fe8d13727c650c7976/m/1/068a34d4-3c8e-41ea-9d42-=
c359aedfea19.png" style=3D"border-radius:50%;display:block;padding:0px;heig=
ht:auto;width:100%;text-align:center;border:0px none transparent" width=3D"=
67"></a></td><td class=3D"m_-8463748081042192912serifLF" style=3D"vertical-=
align:middle;font-family:EconomistSerifLF,Georgia,TimesNewRoman,Times New R=
oman,Times,serif;font-size:18px;color:#121212;line-height:25px;text-align:l=
eft" valign=3D"middle">
								<p style=3D"margin:0">
									<b><a href=3D"https://click.e.economist.com/?qs=3D6eaea0acd4a83136=
3b6035d72a0348a52c7bcced17a09fc0a263e670ebd297a5015d2cf1dd8930643e2802a5764=
188a881718e640818d263" style=3D"color:#000000;text-decoration:none" title=
=3D"" target=3D"_blank">Joshua Spencer</a></b><br>
									News editor</p></td></tr></tbody></table></td></tr></tbody></table=
></td></tr></tbody></table><table cellpadding=3D"0" cellspacing=3D"0" width=
=3D"100%" role=3D"presentation" style=3D"min-width:100%"><tbody><tr><td><ta=
ble align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cel=
lspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"100=
%">
=09
		<tbody><tr>
			<td style=3D"padding:0px 16px 0px 16px" valign=3D"top">
				<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
				=09
						<tbody><tr>
							<td class=3D"m_-8463748081042192912article-text" style=3D"padding:0p=
x 0px 1px;text-align:left;color:rgb(18,18,18);line-height:25px;font-family:=
EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size:18=
px" valign=3D"top">
								<table cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" wi=
dth=3D"100%">
								=09
										<tbody><tr>
											<td>
												<table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpa=
dding=3D"0" cellspacing=3D"0" role=3D"presentation" width=3D"100%">
												=09
														<tbody><tr>
															<td valign=3D"top">
																<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" rol=
e=3D"presentation" width=3D"100%">
																=09
																		<tbody><tr>
																			<td valign=3D"top">
																				Good morning. In today=E2=80=99s edition: Israel releas=
es inquiry into hospital attack, Europe rallies behind Moldova and the batt=
le for surfing=E2=80=99s crown begins.<br>
																				<br>
																				Elsewhere in <i>The Economist</i>: reconsidering your h=
oliday to America? We turn to the data to find out whether the country is r=
eally <a href=3D"https://click.e.economist.com/?qs=3D6eaea0acd4a83136bbf3f6=
e6775064b70660432e453f1ffcdf28bcea66888b25b6a8d44f2c97793d2a6e86dfda1453ece=
58c8e6089c7bac1" style=3D"text-decoration:none" title=3D"losing its appeal =
among foreign tourists" target=3D"_blank">losing its appeal among foreign t=
ourists</a>.</td><td valign=3D"top">
																			</td></tr></tbody></table></td></tr></tbody></table></td=
></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><=
/td></tr></tbody></table><table cellpadding=3D"0" cellspacing=3D"0" width=
=3D"100%" role=3D"presentation" style=3D"min-width:100%"><tbody><tr><td><ta=
ble align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cel=
lspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"100=
%">
=09
		<tbody><tr>
			<td style=3D"padding:0 16px 24px 16px" valign=3D"top">
				<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
				=09
						<tbody><tr>
						</tr></tbody></table></td></tr></tbody></table></td></tr></tbody></ta=
ble><table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"prese=
ntation" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center" bg=
color=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"=
presentation" style=3D"max-width:600px" width=3D"100%">
=09
		<tbody><tr>
			<td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 26px =
16px" valign=3D"top">
				<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
				=09
						<tbody><tr>
							<td style=3D"padding:0 0 0 0" valign=3D"top">
								<h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;font=
-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-=
size:29px;font-weight:bold;color:#121212;line-height:35px;text-align:left">
									<b>Today=E2=80=99s top stories</b></h2></td></tr></tbody></table><=
/td></tr></tbody></table></td></tr></tbody></table>=20

=20



<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"left" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td align=3D"left" class=3D"m_-8463748081042192912prl-12" style=3D"font-=
size:0;padding:0px 16px 24px 16px" valign=3D"top">
    <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bloc=
k;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:20px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" style=3D"p=
adding:2px 0 0 0" valign=3D"top" width=3D"20">
         <img height=3D"auto" role=3D"presentation" src=3D"https://image.e.=
economist.com/lib/fe8d13727c650c7976/m/1/078ee7a6-4ef1-412f-9315-3cbecfea9e=
94.png" style=3D"display:block;width:20px;max-width:20px;height:auto;paddin=
g:0px;border:0px none transparent" width=3D"20"></td></tr><tr>
       </tr></tbody></table></div><div style=3D"display:inline-block;vertic=
al-align:top">
     <table bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912mob-w-spacer" role=3D"presentation" s=
tyle=3D"width:12px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" height=3D"=
12" style=3D"padding:0 0 0 0" valign=3D"top" width=3D"12">
        </td></tr></tbody></table></div><div class=3D"m_-846374808104219291=
2fluid" style=3D"display:inline-block;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:536px">
     =20
       <tbody><tr>
        <td align=3D"left" bgcolor=3D"#ffffff" class=3D"m_-8463748081042192=
912stack m_-8463748081042192912article-text" style=3D"padding:0 0;font-fami=
ly:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size=
:18px;color:#0d0d0d;line-height:25px;text-align:left" valign=3D"top" width=
=3D"50%">
         An =E2=80=9Cinitial inquiry=E2=80=9D released by the <b>Israel Def=
ence Forces </b>claimed troops attacked Nasser hospital in southern <b>Gaza=
</b> on Monday after identifying a =E2=80=9Ccamera that was positioned by H=
amas=E2=80=9D. At least 20 people were killed, <a href=3D"https://click.e.e=
conomist.com/?qs=3D4c03d7505d8b6cb23f624642bc56200228c65a8399637f8b1e585e52=
9a35a41e83c016a761816b4ff6c65e92d3bf464ff115d9aa76ef7ab2" target=3D"_blank"=
>including five journalists</a>. On Tuesday the <small>UN</small> said that=
 there =E2=80=9Cneeds to be justice=E2=80=9D for the attack. Meanwhile prot=
esters in Israel called for the release of hostages and an end to the war.<=
/td></tr></tbody></table></div></td></tr></tbody></table></td></tr></tbody>=
</table>=20
=20

=20



<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"left" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td align=3D"left" class=3D"m_-8463748081042192912prl-12" style=3D"font-=
size:0;padding:0px 16px 24px 16px" valign=3D"top">
    <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bloc=
k;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:20px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" style=3D"p=
adding:2px 0 0 0" valign=3D"top" width=3D"20">
         <img height=3D"auto" role=3D"presentation" src=3D"https://image.e.=
economist.com/lib/fe8d13727c650c7976/m/1/078ee7a6-4ef1-412f-9315-3cbecfea9e=
94.png" style=3D"display:block;width:20px;max-width:20px;height:auto;paddin=
g:0px;border:0px none transparent" width=3D"20"></td></tr><tr>
       </tr></tbody></table></div><div style=3D"display:inline-block;vertic=
al-align:top">
     <table bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912mob-w-spacer" role=3D"presentation" s=
tyle=3D"width:12px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" height=3D"=
12" style=3D"padding:0 0 0 0" valign=3D"top" width=3D"12">
        </td></tr></tbody></table></div><div class=3D"m_-846374808104219291=
2fluid" style=3D"display:inline-block;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:536px">
     =20
       <tbody><tr>
        <td align=3D"left" bgcolor=3D"#ffffff" class=3D"m_-8463748081042192=
912stack m_-8463748081042192912article-text" style=3D"padding:0 0;font-fami=
ly:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size=
:18px;color:#0d0d0d;line-height:25px;text-align:left" valign=3D"top" width=
=3D"50%">
         <b>Donald Trump</b> said he had several =E2=80=9Cgood people=E2=80=
=9D in mind to replace <b>Lisa Cook </b>on the Federal Reserve=E2=80=99s bo=
ard, but that he would abide by any court decision that left her in her job=
. Ms Cook=E2=80=99s lawyers indicated that she would sue to block <a href=
=3D"https://click.e.economist.com/?qs=3D4c03d7505d8b6cb20967b40c7f2dfb7eedf=
e586f481373e7ff1f74be581853ca02f4546c5dedc40c64746124fbf5e86d6049db8901df3a=
a0" target=3D"_blank">Mr Trump=E2=80=99s<b> </b>=E2=80=9Cillegal=E2=80=9D a=
ttempt to sack her</a>. She is alleged to have made false statements on her=
 mortgage.</td></tr></tbody></table></div></td></tr></tbody></table></td></=
tr></tbody></table>=20

=20

=20



<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"left" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td align=3D"left" class=3D"m_-8463748081042192912prl-12" style=3D"font-=
size:0;padding:0px 16px 24px 16px" valign=3D"top">
    <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bloc=
k;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:20px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" style=3D"p=
adding:2px 0 0 0" valign=3D"top" width=3D"20">
         <img height=3D"auto" role=3D"presentation" src=3D"https://image.e.=
economist.com/lib/fe8d13727c650c7976/m/1/078ee7a6-4ef1-412f-9315-3cbecfea9e=
94.png" style=3D"display:block;width:20px;max-width:20px;height:auto;paddin=
g:0px;border:0px none transparent" width=3D"20"></td></tr><tr>
       </tr></tbody></table></div><div style=3D"display:inline-block;vertic=
al-align:top">
     <table bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912mob-w-spacer" role=3D"presentation" s=
tyle=3D"width:12px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" height=3D"=
12" style=3D"padding:0 0 0 0" valign=3D"top" width=3D"12">
        </td></tr></tbody></table></div><div class=3D"m_-846374808104219291=
2fluid" style=3D"display:inline-block;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:536px">
     =20
       <tbody><tr>
        <td align=3D"left" bgcolor=3D"#ffffff" class=3D"m_-8463748081042192=
912stack m_-8463748081042192912article-text" style=3D"padding:0 0;font-fami=
ly:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size=
:18px;color:#0d0d0d;line-height:25px;text-align:left" valign=3D"top" width=
=3D"50%">
         <b>SpaceX=E2=80=99s Starship, </b>the world=E2=80=99s largest and =
most powerful rocket, made it up to space and back down to Earth during its=
 tenth test flight. The largely successful mission is a boost for Elon Musk=
, SpaceX=E2=80=99s boss. The previous three tests of the <a href=3D"https:/=
/click.e.economist.com/?qs=3D4c03d7505d8b6cb2875e5a65076082a5b132ca338b4606=
00278afefdb3a29baf4baa069ed5d5dd92668a03caedfb9a0c61a20eeae2c7e454" target=
=3D"_blank">Starship launch system</a> all failed to meet their intended go=
als. One blew up on the ground in June.</td></tr></tbody></table></div></td=
></tr></tbody></table></td></tr></tbody></table>=20

=20

=20



<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"left" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td align=3D"left" class=3D"m_-8463748081042192912prl-12" style=3D"font-=
size:0;padding:0px 16px 24px 16px" valign=3D"top">
    <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bloc=
k;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:20px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" style=3D"p=
adding:2px 0 0 0" valign=3D"top" width=3D"20">
         <img height=3D"auto" role=3D"presentation" src=3D"https://image.e.=
economist.com/lib/fe8d13727c650c7976/m/1/078ee7a6-4ef1-412f-9315-3cbecfea9e=
94.png" style=3D"display:block;width:20px;max-width:20px;height:auto;paddin=
g:0px;border:0px none transparent" width=3D"20"></td></tr><tr>
       </tr></tbody></table></div><div style=3D"display:inline-block;vertic=
al-align:top">
     <table bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912mob-w-spacer" role=3D"presentation" s=
tyle=3D"width:12px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" height=3D"=
12" style=3D"padding:0 0 0 0" valign=3D"top" width=3D"12">
        </td></tr></tbody></table></div><div class=3D"m_-846374808104219291=
2fluid" style=3D"display:inline-block;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:536px">
     =20
       <tbody><tr>
        <td align=3D"left" bgcolor=3D"#ffffff" class=3D"m_-8463748081042192=
912stack m_-8463748081042192912article-text" style=3D"padding:0 0;font-fami=
ly:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size=
:18px;color:#0d0d0d;line-height:25px;text-align:left" valign=3D"top" width=
=3D"50%">
         Officials in <b>Pakistan</b> warned that the Punjab region faces =
=E2=80=9Cvery high to exceptionally high=E2=80=9D danger of flooding. Earli=
er this week India alerted its neighbour about possible cross-border floodi=
ng as it planned to release water from overflowing dams. It was the first p=
ublic contact between the countries since a <a href=3D"https://click.e.econ=
omist.com/?qs=3D4c03d7505d8b6cb20a10f4f272afba02fc117e780ddc4a46404f45c2483=
77eb94d6c9712794b8f8747fe7099b347a184c35e4ac29ad4d7e2" target=3D"_blank">fo=
ur-day conflict</a> in May. Weeks of heavy rain have battered the region. R=
escuers have evacuated more than 150,000 people.</td></tr></tbody></table><=
/div></td></tr></tbody></table></td></tr></tbody></table>=20

=20

=20



<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"left" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td align=3D"left" class=3D"m_-8463748081042192912prl-12" style=3D"font-=
size:0;padding:0px 16px 24px 16px" valign=3D"top">
    <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bloc=
k;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:20px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" style=3D"p=
adding:2px 0 0 0" valign=3D"top" width=3D"20">
         <img height=3D"auto" role=3D"presentation" src=3D"https://image.e.=
economist.com/lib/fe8d13727c650c7976/m/1/078ee7a6-4ef1-412f-9315-3cbecfea9e=
94.png" style=3D"display:block;width:20px;max-width:20px;height:auto;paddin=
g:0px;border:0px none transparent" width=3D"20"></td></tr><tr>
       </tr></tbody></table></div><div style=3D"display:inline-block;vertic=
al-align:top">
     <table bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912mob-w-spacer" role=3D"presentation" s=
tyle=3D"width:12px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" height=3D"=
12" style=3D"padding:0 0 0 0" valign=3D"top" width=3D"12">
        </td></tr></tbody></table></div><div class=3D"m_-846374808104219291=
2fluid" style=3D"display:inline-block;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:536px">
     =20
       <tbody><tr>
        <td align=3D"left" bgcolor=3D"#ffffff" class=3D"m_-8463748081042192=
912stack m_-8463748081042192912article-text" style=3D"padding:0 0;font-fami=
ly:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size=
:18px;color:#0d0d0d;line-height:25px;text-align:left" valign=3D"top" width=
=3D"50%">
         <b>Howard Lutnick</b> hinted that the Trump administration was con=
sidering buying stakes in <b>defence companies</b>. Speaking to <small>CNBC=
</small>, the commerce secretary called Lockheed Martin, an arms manufactur=
er, =E2=80=9Cbasically an arm of the <small>US</small> government=E2=80=9D =
and said that defence procurement had =E2=80=9Cbeen a giveaway=E2=80=9D. Lo=
ckheed=E2=80=99s shares jumped on the news. Last week America=E2=80=99s gov=
ernment took a 10% stake in <a href=3D"https://click.e.economist.com/?qs=3D=
4c03d7505d8b6cb254da71222c6077acb0274846a8270aae9a6c18f118bcaf57bbab0c580bf=
e7ce032a08d086ef474b08d7c5962e9ce8963" target=3D"_blank">Intel</a>, an aili=
ng chipmaker.</td></tr></tbody></table></div></td></tr></tbody></table></td=
></tr></tbody></table>=20

=20

=20



<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"left" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td align=3D"left" class=3D"m_-8463748081042192912prl-12" style=3D"font-=
size:0;padding:0px 16px 24px 16px" valign=3D"top">
    <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bloc=
k;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:20px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" style=3D"p=
adding:2px 0 0 0" valign=3D"top" width=3D"20">
         <img height=3D"auto" role=3D"presentation" src=3D"https://image.e.=
economist.com/lib/fe8d13727c650c7976/m/1/078ee7a6-4ef1-412f-9315-3cbecfea9e=
94.png" style=3D"display:block;width:20px;max-width:20px;height:auto;paddin=
g:0px;border:0px none transparent" width=3D"20"></td></tr><tr>
       </tr></tbody></table></div><div style=3D"display:inline-block;vertic=
al-align:top">
     <table bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912mob-w-spacer" role=3D"presentation" s=
tyle=3D"width:12px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" height=3D"=
12" style=3D"padding:0 0 0 0" valign=3D"top" width=3D"12">
        </td></tr></tbody></table></div><div class=3D"m_-846374808104219291=
2fluid" style=3D"display:inline-block;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:536px">
     =20
       <tbody><tr>
        <td align=3D"left" bgcolor=3D"#ffffff" class=3D"m_-8463748081042192=
912stack m_-8463748081042192912article-text" style=3D"padding:0 0;font-fami=
ly:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size=
:18px;color:#0d0d0d;line-height:25px;text-align:left" valign=3D"top" width=
=3D"50%">
         <b>Trump Media and Technology Group</b>, the Trump family=E2=80=99=
s media firm, said it would create a =E2=80=9Cdigital asset treasury compan=
y=E2=80=9D with Crypto.com, a currency exchange, and Yorkville Acquisition,=
 a blank-cheque firm. The new company plans to raise $6.4bn to buy <small>C=
RO</small>, the digital token native to Crypto.com. America=E2=80=99s presi=
dent <a href=3D"https://click.e.economist.com/?qs=3D4c03d7505d8b6cb210aa42c=
f899a2918e747ac101efdf0740c690edb4d63d4aec5a0183760109f0ea31cfdd5dda9385041=
462d07f7cf3f20" target=3D"_blank">favours crypto-friendly laws</a>; his fam=
ily has gradually expanded its digital-asset portfolio.</td></tr></tbody></=
table></div></td></tr></tbody></table></td></tr></tbody></table>=20

=20

=20



<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"left" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td align=3D"left" class=3D"m_-8463748081042192912prl-12" style=3D"font-=
size:0;padding:0px 16px 24px 16px" valign=3D"top">
    <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bloc=
k;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:20px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" style=3D"p=
adding:2px 0 0 0" valign=3D"top" width=3D"20">
         <img height=3D"auto" role=3D"presentation" src=3D"https://image.e.=
economist.com/lib/fe8d13727c650c7976/m/1/078ee7a6-4ef1-412f-9315-3cbecfea9e=
94.png" style=3D"display:block;width:20px;max-width:20px;height:auto;paddin=
g:0px;border:0px none transparent" width=3D"20"></td></tr><tr>
       </tr></tbody></table></div><div style=3D"display:inline-block;vertic=
al-align:top">
     <table bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912mob-w-spacer" role=3D"presentation" s=
tyle=3D"width:12px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" height=3D"=
12" style=3D"padding:0 0 0 0" valign=3D"top" width=3D"12">
        </td></tr></tbody></table></div><div class=3D"m_-846374808104219291=
2fluid" style=3D"display:inline-block;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:536px">
     =20
       <tbody><tr>
        <td align=3D"left" bgcolor=3D"#ffffff" class=3D"m_-8463748081042192=
912stack m_-8463748081042192912article-text" style=3D"padding:0 0;font-fami=
ly:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size=
:18px;color:#0d0d0d;line-height:25px;text-align:left" valign=3D"top" width=
=3D"50%">
         Abdulkadir Uraloglu, <b>Turkey=E2=80=99s</b> transport minister, w=
as fined around 9,000 lira ($220) after sharing a video of himself on socia=
l-media driving at 225kph, more than 80kph above the speed limit. The clip =
showed him listening to speeches by <a href=3D"https://click.e.economist.co=
m/?qs=3D4c03d7505d8b6cb267d177a6fe93f91fce9af573ec83bb4a580ee492f2c00f9b98e=
5bc43a50db182a8b8fc101712ad11627541ceb6f4f001" target=3D"_blank">Recep Tayy=
ip Erdogan</a>, Turkey=E2=80=99s president, and Turkish folk music. He adde=
d the hashtag #TurkeyAccelerates. He later apologised for speeding =E2=80=
=9Cunintentionally=E2=80=9D.</td></tr></tbody></table></div></td></tr></tbo=
dy></table></td></tr></tbody></table>=20

=20

=20


=20

=20



<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"left" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td align=3D"left" class=3D"m_-8463748081042192912prl-12" style=3D"font-=
size:0;padding:0px 16px 24px 16px" valign=3D"top">
    <div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-bloc=
k;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:20px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" style=3D"p=
adding:2px 0 0 0" valign=3D"top" width=3D"20">
         <img height=3D"auto" role=3D"presentation" src=3D"https://image.e.=
economist.com/lib/fe8d13727c650c7976/m/1/078ee7a6-4ef1-412f-9315-3cbecfea9e=
94.png" style=3D"display:block;width:20px;max-width:20px;height:auto;paddin=
g:0px;border:0px none transparent" width=3D"20"></td></tr><tr>
       </tr></tbody></table></div><div style=3D"display:inline-block;vertic=
al-align:top">
     <table bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=
=3D"0" class=3D"m_-8463748081042192912mob-w-spacer" role=3D"presentation" s=
tyle=3D"width:12px">
     =20
       <tbody><tr>
        <td align=3D"left" class=3D"m_-8463748081042192912stack" height=3D"=
12" style=3D"padding:0 0 0 0" valign=3D"top" width=3D"12">
        </td></tr></tbody></table></div><div class=3D"m_-846374808104219291=
2fluid" style=3D"display:inline-block;vertical-align:top">
     <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" class=3D"m_-84=
63748081042192912fluid" role=3D"presentation" style=3D"width:536px">
     =20
       <tbody><tr>
        <td align=3D"left" bgcolor=3D"#ffffff" class=3D"m_-8463748081042192=
912stack m_-8463748081042192912article-text" style=3D"padding:0 0;font-fami=
ly:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,serif;font-size=
:18px;color:#0d0d0d;line-height:25px;text-align:left" valign=3D"top" width=
=3D"50%">
         <i>Donald Trump=E2=80=99s presidency has brought exceptional chang=
es to American politics. Read <a href=3D"https://click.e.economist.com/?qs=
=3D4c03d7505d8b6cb2de354c58b7dbca1ba06aeaa6cf59334eec32017ec612f7b55bc94452=
983d9d3317bb12e3eaeb69000a8fc221b99ec01b" target=3D"_blank">The US in brief=
</a>, a daily update of the domestic political stories that matter.</i></td=
></tr></tbody></table></div></td></tr></tbody></table></td></tr></tbody></t=
able>=20

=20

=20


<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td> </td></tr></tbody></table><ta=
ble cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentation=
" style=3D"min-width:100%"><tbody><tr><td> <table align=3D"center" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=09
		<tbody><tr>
			<td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 26px =
16px" valign=3D"top">
				<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
				=09
						<tbody><tr>
							<td style=3D"padding:0 0 0 0;font-size:0;text-align:center" valign=
=3D"top">
								<div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-=
block;width:100%;min-width:100%;max-width:292px;vertical-align:top">
									<p>
									</p><table align=3D"left" border=3D"0" cellpadding=3D"0" cellspaci=
ng=3D"0" role=3D"presentation" width=3D"100%">
									</table></div></td></tr><tr>
						</tr><tr>
							</tr><tr>
							<td align=3D"center" style=3D"padding:0 0px 0px 0px" valign=3D"top">
								<hr style=3D"width:100%;max-width:568px;height:1px;margin:0;backgro=
und-color:#0d0d0d;color:#d7d7d7;border-width:0">
							</td></tr></tbody></table></td></tr></tbody></table><table align=3D"=
center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0=
" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=09
		<tbody><tr>
			<td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 33px =
16px" valign=3D"top">
				<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
				=09
						<tbody><tr>
							<td class=3D"m_-8463748081042192912article-text" style=3D"padding:0 =
0 0 0;font-family:EconomistSerifOsF,ui-serif,Georgia,Times,Times New Roman,=
serif;font-size:18px;color:#121212;line-height:25px;text-align:center" vali=
gn=3D"top">
								<b>Figure of the day:</b> 54,000, the number of exit bans issued by=
 Chinese courts last year, more than double the 24,000 in 2022. <a href=3D"=
https://click.e.economist.com/?qs=3D4c03d7505d8b6cb2afe14c0ec5aa0cbc85d2742=
892362f184a0acfd06c5e3b81f2f9adfe5a7045b40b869029da237fa0540bd21b0ac45ad5" =
target=3D"_blank">Read the full story</a>.</td></tr></tbody></table></td></=
tr></tbody></table> <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0=
" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-wi=
dth:600px" width=3D"100%">
=09
		<tbody><tr>
			<td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 16px =
16px" valign=3D"top">
				<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
				=09
						<tbody><tr>
							<td style=3D"padding:0 0 0 0;font-size:0;text-align:center" valign=
=3D"top">
								<div class=3D"m_-8463748081042192912fluid" style=3D"display:inline-=
block;width:100%;min-width:100%;max-width:292px;vertical-align:top">
									<p>
									</p><table align=3D"left" border=3D"0" cellpadding=3D"0" cellspaci=
ng=3D"0" role=3D"presentation" width=3D"100%">
									</table></div></td></tr><tr>
						</tr><tr>
							</tr><tr>
							<td align=3D"center" style=3D"padding:0 0px 0px 0px" valign=3D"top">
								<hr style=3D"width:100%;max-width:568px;height:1px;margin:0;backgro=
und-color:#0d0d0d;color:#d7d7d7;border-width:0">
							</td></tr></tbody></table></td></tr></tbody></table> </td></tr></tbo=
dy></table><table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=
=3D"presentation" style=3D"min-width:100%"><tbody><tr><td>
<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td>

 <table width=3D"100%" align=3D"center" bgcolor=3D"#ffffff" cellspacing=3D"=
0" cellpadding=3D"0" border=3D"0" role=3D"presentation" style=3D"max-width:=
600px">
    <tbody><tr>
     <td valign=3D"top" align=3D"center">
        <a href=3D"https://click.e.economist.com/u/?qs=3D6eaea0acd4a8313643=
ffdffb00d1835012f29530ce0869fb231712682acea2ff071a1b6a308653279a8b3efde60ee=
8dacf30f1d577b63106233d646f3c2b3dfb" target=3D"_blank">
          <img src=3D"https://pas.economist.com/view/2/39682/4d3a2e8304eb98=
061411f3051e4142e5/2103027?ad_region=3DEurope&amp;ad_country=3DUkraine&amp;=
send_date=3D26/08/2025" style=3D"display:block;max-width:100%;height:auto">
        </a>
        <img width=3D"1" height=3D"1" style=3D"display:none" alt=3D"timer" =
src=3D"https://pas.economist.com/t/2/39682/0033z000035LcCMAA0/2103027?pid=
=3D1&amp;ad_region=3DEurope&amp;ad_country=3DUkraine&amp;send_date=3D26/08/=
2025">
        <img width=3D"1" height=3D"1" style=3D"display:none" alt=3D"trk_px"=
 src=3D"https://pas.economist.com/extt/2/39682/0033z000035LcCMAA0/2103027?p=
id=3D1&amp;ad_region=3DEurope&amp;ad_country=3DUkraine&amp;send_date=3D26/0=
8/2025">
      </td>
    </tr>
  </tbody></table></td></tr></tbody></table></td></tr></tbody></table>
       =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center=
" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=
=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=09
		<tbody><tr>
			<td class=3D"m_-8463748081042192912prl-12" style=3D"padding:16px 16px 26=
px 16px" valign=3D"top">
				<table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
				=09
						<tbody><tr>
							<td style=3D"padding:0 0 0 0" valign=3D"top">
								<h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;font=
-family:-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Helvetica,Arial=
,sans-serif;font-size:29px;font-weight:bold;color:#121212;line-height:35px;=
text-align:left">
									<b>The day ahead</b></h2></td></tr><tr>
							<td style=3D"padding:0 0 0 0;font-family:&#39;EconSansOSLig&#39;,&#3=
9;EconSansOS&#39;,&#39;EconSansOSSec&#39;,-apple-system,BlinkMacSystemFont,=
&#39;Segoe UI&#39;,Helvetica,Arial,sans-serif;font-size:23px;color:#0d0d0d;=
line-height:28px;text-align:left;font-weight:300" valign=3D"top">
							</td></tr></tbody></table></td></tr></tbody></table></td></tr></tbod=
y></table>
       =20
        =20

=20
=20
=20








<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center" bgcolo=
r=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"pres=
entation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 30px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td style=3D"padding:0 0 0 0" valign=3D"top">
        <h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;font=
-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-=
size:23px;font-weight:bold;color:#121212;line-height:28px;text-align:left">
         <b>Donald Trump=E2=80=99s war on the Fed</b></h2></td></tr></tbody=
></table></td></tr></tbody></table>  <table align=3D"center" bgcolor=3D"#ff=
ffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation=
" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D"0=
" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img alt=3D"Federal Reserve Governor Lisa Cook attends the Federal =
Reserve Bank of Kansas City&#39;s 2025 Jackson Hole economic symposium, " s=
rc=3D"https://www.economist.com/content-assets/images/20250830_ibp311.jpg" =
style=3D"display:block;width:100%;max-width:600px;height:auto;padding:0px;t=
ext-align:center;border:none" width=3D"600"></td></tr></tbody></table></td>=
</tr></tbody></table> <table align=3D"center" bgcolor=3D"#ffffff" border=3D=
"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-=
width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D=
"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912econsans" style=3D"padding:4px 0 =
24px 0;margin:0;font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Ar=
ial,sans-serif;font-size:14px;font-weight:400;color:#595959;line-height:20p=
x;text-align:left" valign=3D"top">
        REUTERS </td></tr></tbody></table></td></tr></tbody></table>   <tab=
le align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cell=
spacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"100%=
">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0px 1=
6px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        On Sunday Donald Trump declared that he wanted to <a href=3D"https:=
//click.e.economist.com/?qs=3D4c03d7505d8b6cb20967b40c7f2dfb7eedfe586f48137=
3e7ff1f74be581853ca02f4546c5dedc40c64746124fbf5e86d6049db8901df3aa0" target=
=3D"_blank">fire Lisa Cook</a>, a governor of the Federal Reserve, over cla=
ims she had lied on mortgage applications. Ms Cook has not been charged wit=
h any crime, although the Department of Justice says it plans to open an in=
vestigation. She has refused to resign, calling her would-be sacking unlawf=
ul.<br>
<br>Pressure on the Fed has been rising for months. Mr Trump wants the cent=
ral bank to cut interest rates faster=E2=80=94a tall order when tariffs hav=
e kept inflation above its 2% target. He has mused about firing Jerome Powe=
ll, its chairman, citing a costly renovation of the Fed=E2=80=99s offices i=
n Washington as a potential pretext. But the president=E2=80=99s power to d=
ismiss top Fed officials is legally uncertain and, so far, untested. A Supr=
eme Court ruling from 1935 prevents the president from firing governors =E2=
=80=9Cwithout cause=E2=80=9D. But <a href=3D"https://click.e.economist.com/=
?qs=3D4c03d7505d8b6cb238f9abd047450f861fb11f40a09ae2a92e384f4d8395f67ac11b8=
baa8b988e5b9590d689825cf40f34d94b7a0844cb9b" target=3D"_blank">recent rulin=
gs</a> by the justices have weakened that precedent. What happens next will=
 be up to the courts.<br><br></td></tr></tbody></table></td></tr></tbody></=
table>  =20
<table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" =
cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"=
100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0px 16px 24p=
x 16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img role=3D"presentation" src=3D"https://image.e.economist.com/lib=
/fe8d13727c650c7976/m/8/baea813f-47f4-4a00-b8d1-f14f841ce9f6.jpg" style=3D"=
display:block;width:100%;max-width:568px;height:auto;padding:0px;text-align=
:center;border:none" width=3D"568"></td></tr></tbody></table></td></tr></tb=
ody></table> </td></tr></tbody></table>=20
=20

=20
=20
=20








<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center" bgcolo=
r=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"pres=
entation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 30px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td style=3D"padding:0 0 0 0" valign=3D"top">
        <h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;font=
-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-=
size:23px;font-weight:bold;color:#121212;line-height:28px;text-align:left">
         <b>China clouds Nvidia=E2=80=99s horizon</b></h2></td></tr></tbody=
></table></td></tr></tbody></table>  <table align=3D"center" bgcolor=3D"#ff=
ffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation=
" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D"0=
" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img alt=3D"Co-founder, president and CEO of Nvidia Corporation, Je=
nsen Huang, presents NVIDIA Blackwell GPU as he delivers his keynote speech=
 ahead of the COMPUTEX trade show, in Taipei, Taiwan." src=3D"https://www.e=
conomist.com/content-assets/images/20250830_ibp305.jpg" style=3D"display:bl=
ock;width:100%;max-width:600px;height:auto;padding:0px;text-align:center;bo=
rder:none" width=3D"600"></td></tr></tbody></table></td></tr></tbody></tabl=
e> <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"=
0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D=
"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912econsans" style=3D"padding:4px 0 =
24px 0;margin:0;font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Ar=
ial,sans-serif;font-size:14px;font-weight:400;color:#595959;line-height:20p=
x;text-align:left" valign=3D"top">
        SHUTTERSTOCK </td></tr></tbody></table></td></tr></tbody></table>  =
 <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0"=
 cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D=
"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0px 1=
6px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        Nvidia, an American chipmaker, is expected to issue a strong earnin=
gs report on Wednesday. Booming demand for artificial-intelligence kit amon=
g America=E2=80=99s tech giants continues to drive revenue, especially as s=
hipments of its new Blackwell chips increase. The world=E2=80=99s most valu=
able company has unofficially guided that second-quarter revenues will be $=
45bn, but analysts expect it to beat that by at least $1bn.<br><br>Its thir=
d-quarter outlook could rise to $54bn or more. Whether it can go higher wil=
l depend on geopolitics. Earlier this month, the Trump administration grant=
ed Nvidia permission to resume <a href=3D"https://click.e.economist.com/?qs=
=3D4c03d7505d8b6cb2664d1f38bee0cb1c8086d969ac050afdf51504ac773571430881b0a9=
072c43c35d998e32fbd5a9e5ff640dc6194d6d33" target=3D"_blank">sales to China<=
/a> of its <small>H
</small>20 chips, which Nvidia devised to comply with American export contr=
ols. But the Chinese government warned that the chips were a security risk =
and discouraged customers from buying them. Nvidia is now lobbying Donald T=
rump to allow sales of modified Blackwell chips to China. If it succeeds, r=
evenues could climb. But Mr Trump wants America=E2=80=99s government to rec=
eive a cut of such sales=E2=80=94one that would dent Nvidia=E2=80=99s profi=
ts.<br><br></td></tr></tbody></table></td></tr></tbody></table>  <table ali=
gn=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacin=
g=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0px 16px 32p=
x 16px" valign=3D"top">
    <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D"0=
" role=3D"presentation" style=3D"max-width:336px" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img alt=3D"Chart image" src=3D"https://www.economist.com/content-a=
ssets/images/20250830_IBC393.jpg" style=3D"display:block;width:100%;max-wid=
th:336px;height:auto;padding:0px;text-align:center;border:none" width=3D"33=
6"></td></tr></tbody></table></td></tr></tbody></table>  <table align=3D"ce=
nter" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" =
role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0px 16px 24p=
x 16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img role=3D"presentation" src=3D"https://image.e.economist.com/lib=
/fe8d13727c650c7976/m/8/baea813f-47f4-4a00-b8d1-f14f841ce9f6.jpg" style=3D"=
display:block;width:100%;max-width:568px;height:auto;padding:0px;text-align=
:center;border:none" width=3D"568"></td></tr></tbody></table></td></tr></tb=
ody></table> </td></tr></tbody></table>=20
=20

=20
=20
=20








<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center" bgcolo=
r=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"pres=
entation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 30px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td style=3D"padding:0 0 0 0" valign=3D"top">
        <h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;font=
-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-=
size:23px;font-weight:bold;color:#121212;line-height:28px;text-align:left">
         <b>Europe rallies behind Moldova</b></h2></td></tr></tbody></table=
></td></tr></tbody></table>  <table align=3D"center" bgcolor=3D"#ffffff" bo=
rder=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" style=
=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D"0=
" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img alt=3D"President of Moldova Maia Sandu." src=3D"https://www.ec=
onomist.com/content-assets/images/20250830_ibp309.jpg" style=3D"display:blo=
ck;width:100%;max-width:600px;height:auto;padding:0px;text-align:center;bor=
der:none" width=3D"600"></td></tr></tbody></table></td></tr></tbody></table=
> <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0=
" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D=
"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912econsans" style=3D"padding:4px 0 =
24px 0;margin:0;font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Ar=
ial,sans-serif;font-size:14px;font-weight:400;color:#595959;line-height:20p=
x;text-align:left" valign=3D"top">
        AP </td></tr></tbody></table></td></tr></tbody></table>   <table al=
ign=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspaci=
ng=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0px 1=
6px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        Moldova declared independence from the Soviet Union on August 27th =
1991. On Wednesday France=E2=80=99s president, Germany=E2=80=99s chancellor=
 and Poland=E2=80=99s prime minister will visit to help Maia Sandu, Moldova=
=E2=80=99s president, prevent the country from falling back into <a href=3D=
"https://click.e.economist.com/?qs=3D4c03d7505d8b6cb244bdcb25c6f3b1ea515640=
66cd5c9b5009d00477baee561f5a398c91c7b7d1f1b7d86e829af6771a8e670f45dba0f744"=
 target=3D"_blank">Russia=E2=80=99s orbit</a>. Emmanuel Macron, Friedrich M=
erz and Donald Tusk see Moldova (home to 2.4m people, including Russian and=
 Romanian speakers, and wedged between Ukraine and Romania) as vital to Eur=
opean security.<br><br>Ms Sandu, an anti-corruption campaigner and stalwart=
 ally of Ukraine, has been guiding the country through its candidacy for me=
mbership of the European Union. She was re-elected last year despite facing=
 disinformation and vote-buying, allegedly=20
<a href=3D"https://click.e.economist.com/?qs=3D4c03d7505d8b6cb2a82f020f978e=
e7371a8f26eebeee802accb3c0a6932ae0ff4a15ac02b2773fb188f3dbeacb58afe7bd9075c=
5c1cd59b6" target=3D"_blank">orchestrated</a> by Russia and its allies in M=
oldova. Her party is likely to lose its majority in a parliamentary electio=
n on September 28th. France is particularly concerned. Its cyber-agency wor=
ks closely with Moldova=E2=80=99s, and Mr Macron has his own experience wit=
h Russian meddling. European leaders hope that the high-profile visit helps=
 Ms Sandu shore up support.<br><br></td></tr></tbody></table></td></tr></tb=
ody></table>   <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cel=
lpadding=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:6=
00px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0px 16px 24p=
x 16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img role=3D"presentation" src=3D"https://image.e.economist.com/lib=
/fe8d13727c650c7976/m/8/baea813f-47f4-4a00-b8d1-f14f841ce9f6.jpg" style=3D"=
display:block;width:100%;max-width:568px;height:auto;padding:0px;text-align=
:center;border:none" width=3D"568"></td></tr></tbody></table></td></tr></tb=
ody></table> </td></tr></tbody></table>=20
=20

=20
=20
=20








<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center" bgcolo=
r=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"pres=
entation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 30px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td style=3D"padding:0 0 0 0" valign=3D"top">
        <h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;font=
-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-=
size:23px;font-weight:bold;color:#121212;line-height:28px;text-align:left">
         <b>CrowdStrike rides the AI wave</b></h2></td></tr></tbody></table=
></td></tr></tbody></table>  <table align=3D"center" bgcolor=3D"#ffffff" bo=
rder=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" style=
=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D"0=
" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img alt=3D"The CrowdStrike logo is seen displayed on a smartphone =
screen." src=3D"https://www.economist.com/content-assets/images/20250830_ib=
p308.jpg" style=3D"display:block;width:100%;max-width:600px;height:auto;pad=
ding:0px;text-align:center;border:none" width=3D"600"></td></tr></tbody></t=
able></td></tr></tbody></table> <table align=3D"center" bgcolor=3D"#ffffff"=
 border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" sty=
le=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D=
"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912econsans" style=3D"padding:4px 0 =
24px 0;margin:0;font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Ar=
ial,sans-serif;font-size:14px;font-weight:400;color:#595959;line-height:20p=
x;text-align:left" valign=3D"top">
        GETTY IMAGES </td></tr></tbody></table></td></tr></tbody></table>  =
 <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0"=
 cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D=
"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0px 1=
6px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        On Wednesday CrowdStrike reports quarterly earnings. The outlook fo=
r the American cyber-security giant is strong, reflecting a boom across the=
 sector. Global spending on cyber-security is expected to reach $213bn this=
 year, up from $193bn in 2024. The <small>NASDAQ CTA </small>Cyber-security=
 Index, which tracks big firms that provide digital defences, has jumped by=
 more than 20% in the past 12 months. CrowdStrike=E2=80=99s stock is up by =
more than 55% over the same period.<br><br>Artificial intelligence is the b=
ig driver. Smarter models are improving detection of malware, vulnerabiliti=
es and suspicious network behaviour. Some firms, including CrowdStrike, are=
 also investing in =E2=80=9Cagentic=E2=80=9D systems that respond to threat=
s automatically. But the <small>AI=20
</small>arms race cuts both ways. Criminals are <a href=3D"https://click.e.=
economist.com/?qs=3D4c03d7505d8b6cb221c391beff7da441d879e976d8b1db67175de3f=
edcd1a2a085fbc3ecaaf3f74dd08e330a4c64a4ba0d89d0c7040787c5" target=3D"_blank=
">using the technology</a> to generate stealthier malware and more convinci=
ng phishing lures. In April the <small>FBI </small>reported that America=E2=
=80=99s losses to internet crime in 2024 had surged to $17bn, up by a third=
 on the previous year.<br><br></td></tr></tbody></table></td></tr></tbody><=
/table>   <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadd=
ing=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px"=
 width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0px 16px 24p=
x 16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img role=3D"presentation" src=3D"https://image.e.economist.com/lib=
/fe8d13727c650c7976/m/8/baea813f-47f4-4a00-b8d1-f14f841ce9f6.jpg" style=3D"=
display:block;width:100%;max-width:568px;height:auto;padding:0px;text-align=
:center;border:none" width=3D"568"></td></tr></tbody></table></td></tr></tb=
ody></table> </td></tr></tbody></table>=20
=20

=20
=20
=20








<table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"presentat=
ion" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center" bgcolo=
r=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"pres=
entation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 30px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td style=3D"padding:0 0 0 0" valign=3D"top">
        <h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;font=
-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-=
size:23px;font-weight:bold;color:#121212;line-height:28px;text-align:left">
         <b>The battle for surfing=E2=80=99s crown begins</b></h2></td></tr=
></tbody></table></td></tr></tbody></table>  <table align=3D"center" bgcolo=
r=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"pres=
entation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D"0=
" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img alt=3D"Molly Picklum of Australia surfs in a big wave - Teahup=
oo, Tahiti, French Polynesia." src=3D"https://www.economist.com/content-ass=
ets/images/20250830_ibp307.jpg" style=3D"display:block;width:100%;max-width=
:600px;height:auto;padding:0px;text-align:center;border:none" width=3D"600"=
></td></tr></tbody></table></td></tr></tbody></table> <table align=3D"cente=
r" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" rol=
e=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D=
"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912econsans" style=3D"padding:4px 0 =
24px 0;margin:0;font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Ar=
ial,sans-serif;font-size:14px;font-weight:400;color:#595959;line-height:20p=
x;text-align:left" valign=3D"top">
        GETTY IMAGES </td></tr></tbody></table></td></tr></tbody></table>  =
 <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0"=
 cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D=
"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0px 1=
6px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        On Wednesday the World Surf League opens its nine-day window to cro=
wn its champions for 2025. Surf competitions depend on conditions, which is=
 why the league gives itself more than a week to run the finals. This year =
they are held at Cloudbreak, a remote reef break off the coast of Fiji. Its=
 waves are known for their speed and size, making them some of the most dif=
ficult=E2=80=94and spectacular=E2=80=94in the world to surf.<br><br>The for=
mat rewards consistency. Since January, surfers have competed at 11 locatio=
ns worldwide. The top five men and women now face off in Fiji in head-to-he=
ad heats: fifth versus fourth, the winner against third, and so on, until a=
 challenger meets the top seed.<br>
<br>Australia=E2=80=99s Molly Picklum leads the women=E2=80=99s field, whic=
h also includes two American former champions: Caroline Marks and Caitlin S=
immers. Brazil=E2=80=99s Yago Dora tops the men=E2=80=99s rankings. The sol=
e former champion in the men=E2=80=99s draw is the fifth seed, Italo Ferrei=
ra, but he will need a spectacular run to take the title.<br><br></td></tr>=
</tbody></table></td></tr></tbody></table>   </td></tr></tbody></table>=20
=20

=20
=20
=20






=20

=20
=20
=20






=20

=20
=20
=20







       =20
         <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"=
presentation" style=3D"min-width:100%"><tbody><tr><td> <table align=3D"cent=
er" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" ro=
le=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0px 16px 24p=
x 16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img role=3D"presentation" src=3D"https://image.e.economist.com/lib=
/fe8d13727c650c7976/m/8/baea813f-47f4-4a00-b8d1-f14f841ce9f6.jpg" style=3D"=
display:block;width:100%;max-width:568px;height:auto;padding:0px;text-align=
:center;border:none" width=3D"568"></td></tr></tbody></table></td></tr></tb=
ody></table>=20
<table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" =
cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"=
100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 30px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td style=3D"padding:0 0 0 0" valign=3D"top">
        <h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;font=
-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-=
size:23px;font-weight:bold;color:#121212;line-height:28px;text-align:left">
         <b>Daily quiz</b></h2></td></tr></tbody></table></td></tr></tbody>=
</table><table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpaddin=
g=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" w=
idth=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0px 1=
6px" valign=3D"top">
    <table align=3D"center" border=3D"0" cellpadding=3D"0" cellspacing=3D"0=
" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img alt=3D"" src=3D"https://www.economist.com/content-assets/image=
s/20250616_ibp366.jpg" style=3D"display:block;width:100%;max-width:600px;he=
ight:auto;padding:0px;text-align:center;border:none" width=3D"600"></td></t=
r></tbody></table></td></tr></tbody></table><table align=3D"center" bgcolor=
=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"prese=
ntation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D=
"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912econsans" style=3D"padding:4px 0 =
24px 0;margin:0;font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Ar=
ial,sans-serif;font-size:14px;font-weight:400;color:#595959;line-height:20p=
x;text-align:left" valign=3D"top">
        THE ECONOMIST </td></tr></tbody></table></td></tr></tbody></table><=
table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" c=
ellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"1=
00%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 12px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        <p style=3D"margin:0px 0px;text-align:left;padding:0px 0px 0px 0px"=
>
         <b>Wednesday: </b>Which Bobby Goldsboro song was the best-selling =
record worldwide in 1968?</p></td></tr></tbody></table></td></tr></tbody></=
table><table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=
=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" wi=
dth=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 12px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        <p style=3D"margin:0px 0px;text-align:left;padding:0px 0px 0px 0px"=
>
         <b>Tuesday: </b>What type of people did Karl Marx and Friedrich En=
gels call upon to =E2=80=9Cunite=E2=80=9D in the Communist Manifesto?</p></=
td></tr></tbody></table></td></tr></tbody></table><table align=3D"center" b=
gcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D=
"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 32px =
16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        <p class=3D"m_-8463748081042192912article-text" style=3D"margin:0">
         We will serve you a new question each day this week. On Friday you=
r challenge is to give us all five answers and, as important, tell us the c=
onnecting theme. Email your responses (and include mention of your home cit=
y and country) by 1700 <small>BST</small> on Friday to <a href=3D"mailto:Qu=
izEspresso@economist.com" target=3D"_blank">QuizEspresso@economist.com</a>.=
 We=E2=80=99ll pick randomly from those with the right answers and crown th=
ree winners on Saturday.</p></td></tr></tbody></table></td></tr></tbody></t=
able><table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=
=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" wi=
dth=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0px 16px 24p=
x 16px" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" style=3D"padding:0 0 0 0" valign=3D"top">
        <img role=3D"presentation" src=3D"https://image.e.economist.com/lib=
/fe8d13727c650c7976/m/8/baea813f-47f4-4a00-b8d1-f14f841ce9f6.jpg" style=3D"=
display:block;width:100%;max-width:568px;height:auto;padding:0px;text-align=
:center;border:none" width=3D"568"></td></tr></tbody></table></td></tr></tb=
ody></table> </td></tr></tbody></table>
       =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td><table align=3D"center=
" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=
=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        <br>
        <br>
        =C2=A0</td></tr></tbody></table></td></tr></tbody></table><table al=
ign=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspaci=
ng=3D"0" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        </td></tr></tbody></table></td></tr></tbody></table><table align=3D=
"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D"0" cellspacing=3D"=
0" role=3D"presentation" style=3D"max-width:600px" width=3D"100%">
=20
  <tbody><tr>
   <td class=3D"m_-8463748081042192912prl-12" style=3D"padding:0 16px 0 16p=
x" valign=3D"top">
    <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"present=
ation" width=3D"100%">
    =20
      <tbody><tr>
       <td class=3D"m_-8463748081042192912article-text m_-84637480810421929=
12twib-chunks" style=3D"padding:0 0 1px 0;font-family:EconomistSerifOsF,ui-=
serif,Georgia,Times,Times New Roman,serif;font-size:18px;color:#121212;line=
-height:25px;text-align:left" valign=3D"top">
        </td></tr></tbody></table></td></tr></tbody></table> </td></tr></tb=
ody></table>
       =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td>
<table cellpadding=3D"0" cellspacing=3D"0" role=3D"presentation" style=3D"m=
in-width:100%" width=3D"100%">
=20
  <tbody><tr>
   <td>
    <table align=3D"center" bgcolor=3D"#ffffff" border=3D"0" cellpadding=3D=
"0" cellspacing=3D"0" role=3D"presentation" style=3D"max-width:600px" width=
=3D"100%">
    =20
      <tbody><tr>
       <td align=3D"center" bgcolor=3D"#f5f4ef" class=3D"m_-846374808104219=
2912ph48pw24" style=3D"padding:112px 32px 112px 32px" valign=3D"top">
        <table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" role=3D"pre=
sentation" width=3D"100%">
        =20
          <tbody><tr>
           <td bgcolor=3D"#f5f4ef" style=3D"padding:6px 8px 0 0" valign=3D"=
top" width=3D"27">
            <img alt=3D"" border=3D"0" height=3D"18" src=3D"https://image.e=
.economist.com/lib/fe8d13727c650c7976/m/3/85457470-c0fd-44f8-aaae-7fcbcd6c0=
8eb.png" style=3D"display:block;border:none" width=3D"27"></td><td bgcolor=
=3D"#f5f4ef" style=3D"padding:0 0 28px 0;font-family:EconomistSerifOsF,ui-s=
erif,Georgia,Times,Times New Roman,serif;font-size:29px;color:#0d0d0d;line-=
height:35px;text-align:left" valign=3D"top">
            Words are but the vague shadows of the volumes we mean.</td></t=
r><tr>
           <td style=3D"padding:8px 0 0 0" valign=3D"bottom" width=3D"30">
           </td><td style=3D"text-align:left" valign=3D"top">
            <hr style=3D"width:30px;height:4px;margin:0;background-color:#e=
3120b;color:#e3120b;border-width:0">
           </td></tr><tr>
           <td style=3D"padding:0 0 0 0" valign=3D"top" width=3D"30">
           </td><td style=3D"padding:0 0 0px 0" valign=3D"top">
            <h2 class=3D"m_-8463748081042192912econsans" style=3D"margin:0;=
font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;f=
ont-size:18px;font-weight:bold;color:#0d0d0d;line-height:28px;text-align:le=
ft">
             <b>Theodore Dreiser</b></h2></td></tr></tbody></table></td></t=
r><tr>
       <td height=3D"48" style=3D"font-size:1px;line-height:1px">
        =C2=A0</td></tr></tbody></table></td></tr></tbody></table>
</td></tr></tbody></table>
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
       =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td>


<table role=3D"presentation" style=3D"max-width:600px" width=3D"100%" cells=
pacing=3D"0" cellpadding=3D"0" border=3D"0" bgcolor=3D"#ffffff" align=3D"ce=
nter">
  <tbody><tr>
    <td class=3D"m_-8463748081042192912econsans" style=3D"padding:24px 16px=
 16px 16px;font-family:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,s=
ans-serif;font-size:16px;color:#121212;line-height:25px;text-align:left" va=
lign=3D"top" bgcolor=3D"#e0ebeb">
      <p style=3D"margin:0">
        We=E2=80=99d value your feedback on the World in Brief newsletter. =
You can share your thoughts and suggestions with us directly here:
        <a href=3D"mailto:worldinbrief@economist.com" style=3D"color:#00000=
0;text-decoration:none;border-bottom:1px solid #3c4faf" title=3D"" target=
=3D"_blank">worldinbrief@economist.com</a>.
       =20
      </p>
    </td>
  </tr>
  <tr>
    <td class=3D"m_-8463748081042192912econsans" valign=3D"top" bgcolor=3D"=
#e0ebeb">
      <p style=3D"margin:0">
      </p>
    </td>
  </tr>
  <tr>
    <td style=3D"font-size:1px;line-height:1px" height=3D"32">
    </td>
  </tr>
</tbody></table>

</td></tr></tbody></table>
       =20
         =20
       =20
         =20
        <table role=3D"presentation" style=3D"max-width:600px" width=3D"100=
%" cellspacing=3D"0" cellpadding=3D"0" border=3D"0" bgcolor=3D"#ffffff" ali=
gn=3D"center">
          <tbody>
            <tr>
              <td style=3D"padding:0 16px 40px 16px" valign=3D"top">
                <table role=3D"presentation" width=3D"100%" cellspacing=3D"=
0" cellpadding=3D"0" border=3D"0">
                  <tbody>
                    <tr>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
         =20
        <table cellpadding=3D"0" cellspacing=3D"0" width=3D"100%" role=3D"p=
resentation" style=3D"min-width:100%"><tbody><tr><td>      =20

        <table width=3D"100%" align=3D"center" bgcolor=3D"#ffffff" cellspac=
ing=3D"0" cellpadding=3D"0" border=3D"0" role=3D"presentation" style=3D"max=
-width:600px">
          <tbody><tr>
            <td valign=3D"top" style=3D"padding:0 16px 32px 16px">
              <table width=3D"100%" cellspacing=3D"0" cellpadding=3D"0" bor=
der=3D"0" role=3D"presentation">
                <tbody><tr>
                  <td class=3D"m_-8463748081042192912econsans" valign=3D"to=
p" style=3D"padding:0 0 32px 0;font-family:EconomistSansLF,system-ui,Segoe =
UI,Helvetica,Arial,sans-serif;font-size:14px;color:#595959;line-height:23px=
;text-align:left;border-bottom:1px solid #121212">
                    <p style=3D"margin:0">
                      This email has been sent to:=20
                      <a style=3D"color:#595959;text-decoration:none;border=
-bottom:1px solid #3c4faf">destifor@gmail.com</a>. If you&#39;d like to upd=
ate your details please=20
                      <a href=3D"https://click.e.economist.com/u/?qs=3D4c03=
d7505d8b6cb2a80a0cf568640ac2f7f693fdda238e9ff04c94eed854b1670ca90f78826a6f3=
a2e3d4ee8c05346a53b7d78f3e630142e3e74e1e5fb650ec0" style=3D"color:#595959;t=
ext-decoration:none;border-bottom:1px solid #3c4faf" target=3D"_blank">clic=
k here</a>. Replies to this email will not reach us. If you don&#39;t want =
to receive these updates anymore, please unsubscribe=20
                      =20
                      <a href=3D"https://myaccount.economist.com/s/preferen=
ces?contactId=3D0033z000035LcCMAA0&amp;newslettercode=3Despresso" style=3D"=
color:#595959;text-decoration:none;border-bottom:1px solid #3c4faf" target=
=3D"_blank">here</a>.
                    =20
                    </p>
                  </td>
                </tr>
                <tr>
                  <td align=3D"left" valign=3D"top" style=3D"padding:8px 0 =
16px 0;border-bottom:1px solid #d7d7d7">

                    <table align=3D"left" cellspacing=3D"0" cellpadding=3D"=
0" border=3D"0" role=3D"presentation">
                      <tbody><tr>
                        <td class=3D"m_-8463748081042192912econsans" valign=
=3D"middle" style=3D"vertical-align:middle;padding:8px 16px 0 0;font-family=
:EconomistSansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-size:16=
px;font-weight:bold;color:#121212;line-height:32px;text-align:left">
                          <p style=3D"margin:0">
                            Join the conversation
                          </p>
                        </td>
                      </tr>
                    </tbody></table>
                   =20
                    <table align=3D"left" cellspacing=3D"0" cellpadding=3D"=
0" border=3D"0" role=3D"presentation">
                      <tbody><tr>
              <td valign=3D"top" style=3D"padding:8px 8px 0 0">
                          <a href=3D"https://click.e.economist.com/u/?qs=3D=
4c03d7505d8b6cb2e3368f8650aaf0524945fb3c8862b319f0a06fc73243f0c6e0971602039=
60c58404e71c9715a8b3b8ac0d7827c2a93d13d07a874716fff1a" target=3D"_blank">
                            <img src=3D"https://image.e.economist.com/lib/f=
e8d13727c650c7976/m/1/40e8bc84-2f84-4dad-9c29-2937734b8611.png" width=3D"32=
" height=3D"32" alt=3D"LinkedIn" border=3D"0" style=3D"display:block;border=
:none">
                          </a>
                        </td>
                        <td valign=3D"top" style=3D"padding:8px 6px 0 6px">
                          <a href=3D"https://click.e.economist.com/u/?qs=3D=
4c03d7505d8b6cb2ebd6469d11ec27ca043c0bbb053f7186bad3db3a81f9e8dbd64ddc6bf7b=
10a7b9d7825fcf34311266b018a3a8f767fe3a4e507aff1e5c02b" target=3D"_blank">
                            <img src=3D"https://image.e.economist.com/lib/f=
e8d13727c650c7976/m/1/9567b741-addd-4154-8841-32b806924b3d.png" width=3D"32=
" height=3D"32" alt=3D"Facebook" border=3D"0" style=3D"display:block;border=
:none">
                          </a>
                        </td>
                        <td valign=3D"top" style=3D"padding:8px 6px 0 6px">
                          <a href=3D"https://click.e.economist.com/u/?qs=3D=
4c03d7505d8b6cb29aac58457e6b20b38adfaca1ae7831d94fcf16a140994ab94148957fbfd=
ad4ded8b77fe0e953e35ad3e80b232dea7d7d0e6af37b530039a6" target=3D"_blank">
                            <img src=3D"https://image.e.economist.com/lib/f=
e8d13727c650c7976/m/1/e3c06c10-1ec1-4fd6-8744-1c83de94bca5.png" width=3D"32=
" height=3D"32" alt=3D"X" border=3D"0" style=3D"display:block;border:none">
                          </a>
                        </td>
                        <td valign=3D"top" style=3D"padding:8px 6px 0 6px">
                          <a href=3D"https://click.e.economist.com/u/?qs=3D=
4c03d7505d8b6cb277d5af3f46a05283982eb6a5c6c6d16d8ebeb5dd463f5b61331d86d4760=
df57d20a0cfb96131ef8bd9d3590a1fe0546039d008b38ab6526b" target=3D"_blank">
                            <img src=3D"https://image.e.economist.com/lib/f=
e8d13727c650c7976/m/1/e5846dc9-21af-48a7-836a-8ca6932096bb.png" width=3D"32=
" height=3D"32" alt=3D"Instagram" border=3D"0" style=3D"display:block;borde=
r:none">
                          </a>
                        </td>
                         <td valign=3D"top" style=3D"padding:8px 6px 0 6px"=
>
                          <a href=3D"https://click.e.economist.com/u/?qs=3D=
4c03d7505d8b6cb2ef3aec0587aa41bb9ab9da4984c10c8e350c4f51d87d045cf9fa72a9a65=
181ae0348a11e48a77ad321f1077fe656fc9f9187a98bbda3a1d3" target=3D"_blank">
                            <img src=3D"https://image.e.economist.com/lib/f=
e8d13727c650c7976/m/1/66506051-ccb9-499d-b2d1-dcb38be7e0bc.png" width=3D"32=
" height=3D"32" alt=3D"32" border=3D"0" style=3D"display:block;border:none"=
>
                          </a>
                        </td>
      <td valign=3D"top" style=3D"padding:8px 6px 0 6px">
                          <a href=3D"https://click.e.economist.com/u/?qs=3D=
4c03d7505d8b6cb294cb802a58dc061638b008cc49333a3323b5e67a433e1e32aa5a7a9cb4f=
bd7544102741c1554235a187ad5a15249deaf0fe9e0e1b39f1e88" target=3D"_blank">
                            <img src=3D"https://image.e.economist.com/lib/f=
e8d13727c650c7976/m/1/297e30c2-3f6d-43e4-afb5-6733fd074824.png" width=3D"32=
" height=3D"32" alt=3D"TikTok" border=3D"0" style=3D"display:block;border:n=
one">
                          </a>
                        </td>
                        <td valign=3D"top" style=3D"padding:8px 0 0 6px">
                          <a href=3D"https://click.e.economist.com/u/?qs=3D=
4c03d7505d8b6cb251342262b59d204f7ccccbb9e9c8221391a4b4ec76ff2e940220c048002=
907bb0e6e9ebb814191db149d863edab5b08f80d6c833e0463132" target=3D"_blank">
                            <img src=3D"https://image.e.economist.com/lib/f=
e8d13727c650c7976/m/1/4edbec00-4cd2-456a-81fd-ef86dd5388a2.png" width=3D"32=
" height=3D"32" alt=3D"Youtube" border=3D"0" style=3D"display:block;border:=
none">
                          </a>
                        </td>
                      </tr>
                    </tbody></table>
                   =20
                  </td>
                </tr>
                <tr>
                  <td align=3D"center" valign=3D"top" style=3D"padding:16px=
 0 0 0;font-size:0;text-align:center;border-bottom:1px solid #d7d7d7">
                   =20
                    <div class=3D"m_-8463748081042192912fluid" style=3D"dis=
play:inline-block;width:100%;min-width:100%;max-width:284px;vertical-align:=
top">
                      <table width=3D"100%" align=3D"left" cellspacing=3D"0=
" cellpadding=3D"0" border=3D"0" role=3D"presentation">
                        <tbody><tr>
                          <td class=3D"m_-8463748081042192912econsans" widt=
h=3D"50%" valign=3D"top" style=3D"padding:0 0 16px 0;font-family:EconomistS=
ansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-size:14px;color:#5=
95959;line-height:23px;text-align:left">
                            <p style=3D"margin:0">
                              <a href=3D"https://click.e.economist.com/u/?q=
s=3D4c03d7505d8b6cb28a049696d793d722e7154cb5e01490ba2afbe6b168b889fd0d9a589=
bf21439d4777a34bf1c5beda28f3a2cc5bb748384" style=3D"color:#595959;text-deco=
ration:none" target=3D"_blank">
                                Advertising Info
                              </a>
                            </p>
                          </td>
                          <td class=3D"m_-8463748081042192912econsans" widt=
h=3D"50%" valign=3D"top" style=3D"padding:0 0 16px 0;font-family:EconomistS=
ansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-size:14px;color:#5=
95959;line-height:23px;text-align:left">
                            <p style=3D"margin:0">
                              <a href=3D"https://click.e.economist.com/u/?q=
s=3D4c03d7505d8b6cb2dcebf37a136f265523ca02d10714c429e67810856ea03627ade8f8f=
0b60d5f8e6dbcab4162e8e2f9536c6f366f64cc35808387836f64997d" style=3D"color:#=
595959;text-decoration:none" target=3D"_blank">
                                Terms &amp; Conditions
                              </a>
                            </p>
                          </td>
                        </tr>
                      </tbody></table>
                    </div>
                   =20
                    <div class=3D"m_-8463748081042192912fluid" style=3D"dis=
play:inline-block;width:100%;min-width:100%;max-width:284px;vertical-align:=
top">
                      <table width=3D"100%" align=3D"right" cellspacing=3D"=
0" cellpadding=3D"0" border=3D"0" role=3D"presentation">
                        <tbody><tr>
                          <td class=3D"m_-8463748081042192912econsans" widt=
h=3D"50%" valign=3D"top" style=3D"padding:0 0 16px 0;font-family:EconomistS=
ansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-size:14px;color:#5=
95959;line-height:23px;text-align:left">
                            <p style=3D"margin:0">
                              <a href=3D"https://click.e.economist.com/u/?q=
s=3D4c03d7505d8b6cb27361786a4e713230c0c02b4c0c569c7abf4ead76a9db7e7c40fa54a=
9f9ac3eef030d5a6a43f6e82c42fcced72ebc42106c5e2ff41edce584" style=3D"color:#=
595959;text-decoration:none" target=3D"_blank">
                                Help
                              </a>
                            </p>
                          </td>
                          <td class=3D"m_-8463748081042192912econsans" widt=
h=3D"50%" valign=3D"top" style=3D"padding:0 0 16px 0;font-family:EconomistS=
ansLF,system-ui,Segoe UI,Helvetica,Arial,sans-serif;font-size:14px;color:#5=
95959;line-height:23px;text-align:left">
                            <p style=3D"margin:0">
                              <a href=3D"https://click.e.economist.com/u/?q=
s=3D4c03d7505d8b6cb2bac49db1f48f0ba62257cafcdff891644817f7716edb0a88b794d05=
883f1b499f84a173f43aa0522fae28d96104f83fb49eaa13f1085b404" style=3D"color:#=
595959;text-decoration:none" target=3D"_blank">
                                Privacy Policy
                              </a>
                            </p>
                          </td>
                        </tr>
                      </tbody></table>
                    </div>
                   =20
                  </td>
                </tr>
                <tr>
                  <td class=3D"m_-8463748081042192912econsans" valign=3D"to=
p" style=3D"padding:16px 0 16px 0;font-family:EconomistSansLF,system-ui,Seg=
oe UI,Helvetica,Arial,sans-serif;font-size:14px;color:#595959;line-height:2=
3px;text-align:left;border-bottom:1px solid #d7d7d7">
                    <p style=3D"margin:0">
                      Copyright =C2=A9 The Economist Newspaper Limited 2025=
. All rights reserved.
                    </p>
                  </td>
                </tr>
                <tr>
                  <td class=3D"m_-8463748081042192912econsans" valign=3D"to=
p" style=3D"padding:16px 0 16px 0;font-family:EconomistSansLF,system-ui,Seg=
oe UI,Helvetica,Arial,sans-serif;font-size:14px;color:#595959;line-height:2=
3px;text-align:left;border-bottom:1px solid #121212">
                    <p style=3D"margin:0">
                      Registered in England and Wales.=20
                      <span style=3D"white-space:nowrap">No.236383</span>
                    </p>
                    <div style=3D"display:block;height:8px;font-size:8px;li=
ne-height:8px">=C2=A0
                    </div>
                    <p style=3D"margin:0">
                      Registered office: The Adelphi, 1=E2=80=9311 John Ada=
m Street, London,=20
                      <span style=3D"white-space:nowrap">WC2N 6HT</span>
                    </p>
                  </td>
                </tr>
              </tbody></table>
            </td>
          </tr>
        </tbody></table>
        </td></tr></tbody></table>
                 =20
      </div>
     =20
    </center>
   =20
   =20
    <div style=3D"max-height:0;overflow:hidden">
      This email was sent to:=C2=A0<a href=3D"mailto:destifor@gmail.com" ta=
rget=3D"_blank">destifor@gmail.com</a>
      <br>
      <br>This email was sent by: The Economist Newspaper Ltd., The Adelphi=
, 1-11 John Adam Street, London, London, WC2N 6HT, GB
    </div>
   =20
    </div>

</div></div></div>

--0000000000009c66dc063d592f61--
"""

real_email_4 = """Delivered-To: yevheniia.ilchenko@destilabs.com
Received: by 2002:a05:6838:6527:b2:968:7d74:e7a4 with SMTP id ep7csp263615nkb;
        Wed, 27 Aug 2025 06:58:27 -0700 (PDT)
X-Received: by 2002:a05:6902:340e:b0:e96:c71a:8a19 with SMTP id 3f1490d57ef6-e96c71a9c85mr11051636276.47.1756303107184;
        Wed, 27 Aug 2025 06:58:27 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1756303107; cv=none;
        d=google.com; s=arc-20240605;
        b=YXsY0dTP7cmvN2qHpRUFgydsKw5tI8rCZuEnMBKWl27PRCUNi5csu5q9ZCtmsbE7rJ
         hwQlzQWecn8frclqR4wE9xaWBkkqDTFLwy5bPrXrymv0wpXqHb3VFsuRIWaoO9y70GMH
         UMEwn2SzhH7JV5q3MI8p/DqMMqM9Wpw0hXiW8O2Oe+BTMozDZy1lxKK4ZvPZKlHyNeQc
         ABmLLi735oOkg9/BAGMIAG26ODObBgBD1SFK9mj3TIkNjDxCo3TZZPsJj2v7dKQPn8+Y
         fF7ihFYER2YtZ2hLInd6XUNL6PhUbqH5T4y/GOOc/DCMdGa6DPXxyi+GLWp/WJvWIWnS
         HVRQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :dkim-signature;
        bh=VEHtw7qeESpmLE1eBAs5u4yQ+VHpQ7Sg9XYxS45MZew=;
        fh=HAMlP18b8NkbM3RF1S047V5u0k2J0lYx0FjjO6Xqv0o=;
        b=fi1PK/Mq5IjC57BoLG0DTt5YQZgyNbVpcCwJ2D4OcSuik6abiaJnNqPibAq+io9+kM
         ReJr6PMCu0uqb7M2RMTf6d0hcv1NgyRBgPwPURm+dyq62wiwY/1LjU1q1tO/DqEMHaWo
         ac/93M1/bQ5qEaftob2KBKPOuVHd4T6bTDBcHpfBht7nMxHCg531gdL+4S3vH4ExzqSe
         L3Xn9vJtTXs34mqmVmWnbjrBMbU3FGjMtt40mDwkrUBG5Jk+fImVF7Jy92Wh4cjr9jB5
         7uy81cityocfN83VugcWhoVfxijAYTfdmv4o1qaLbEXURsJmYnY8IdpPttn3RGNyEY1I
         OUGA==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=KxXTOtrI;
       spf=pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=destifor@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=neutral header.i=@destilabs.com
Return-Path: <destifor@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 3f1490d57ef6-e952c341e17sor7067249276.8.2025.08.27.06.58.27
        for <yevheniia.ilchenko@destilabs.com>
        (Google Transport Security);
        Wed, 27 Aug 2025 06:58:27 -0700 (PDT)
Received-SPF: pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=KxXTOtrI;
       spf=pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=destifor@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=neutral header.i=@destilabs.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20230601; t=1756303106; x=1756907906; darn=destilabs.com;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :from:to:cc:subject:date:message-id:reply-to;
        bh=VEHtw7qeESpmLE1eBAs5u4yQ+VHpQ7Sg9XYxS45MZew=;
        b=KxXTOtrIKTg0c7FNuTaF0WOwaIzFYLwqfy+NvDVWKN89Bxo0mGhoTo9efN/1K9KNAZ
         PruvzyzZLENrbKq9WCuBc4q16WJ5zEXQmWiQ+aYtKBFLptLfLJsp33jrYGZqNUSzlhjC
         DdxfQ37c90QzptVlDmyoE+sZ4ut/wTyM7z119j8Q58BWNPq9DfqKgzP1Nzy8Q2QCVaIu
         lkDoQHWWU5rsaINRS0vCmetletq7Dde97m4txZZeTDvQtienXNvVeQl5OfxYpltjuoJK
         8/fAv068MU+Wt5r6/1ZdPnvgMdY+f7OxxResvSNiRWVDt6RhTrc1ftl5UNFuuwlhSf/4
         0h1Q==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1756303106; x=1756907906;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to;
        bh=VEHtw7qeESpmLE1eBAs5u4yQ+VHpQ7Sg9XYxS45MZew=;
        b=U19VQbkdKjpFMbS41JvdjiqgsL6gi49gObtcNgo2YEpM4n3WJvQHordqGWMVINbsMN
         +m73ZlE6v28wC1v/TlIN2bjcAFXfalLpAZdZ3pU1csWgzH/Z20s6gzLe3sTdJ6SWunag
         4zE7Ps7DXr6FB/8H8Pt4nr7XqCslypqm330sgAlPniK1XYIXHH5S0LuT2zMYzpGH7FrH
         4JjTVp3CkEVZKAjWlXs11olXpfenQbl541o8zNRiq7EEQ7jeRG3jsXxMTYRV3Ve0iI88
         O1GQFqJU//bgR7cNFWYINOY/2FUC5QUeQWnt6ZbvHfHJf3Q/LyK6zK6YV4SXINJkJBhs
         colw==
X-Gm-Message-State: AOJu0YyLWl10NW26p+L0zBxkjny8PYzGPLsex85D1Y95tViHMaKqrW0Y
	1qp543hEPTxIJ/u7eLBWD+M2nEC5tkIRatsiFPsJpjUCpW1045ogIpeLOmjRmnhR6UIbMwLtbWQ
	sudA3XVNhHnjzvs/LtndXfcvtBdquW4IYjyJ66Bw=
X-Gm-Gg: ASbGncs62qayrsr97DCK78MCE3YUK+yTVy9/NiVvPVOpms494aSUEhhVTeSkA9Ea0mf
	6AQEtDrlepGfPwvWdaJ1+mamku3QZcdyPBjJDVAS7PNP73DLtTfAn5FoJjZADbfIU5TYNvq4TMm
	oqOfbY3+8oqGRCfCzz7hc9BOtGbKrmMvWCvGTGqJK1pepKqp5SEU19hsQGI/k78hEXapb0cDIiz
	dYIizEq/YZY2bFBHkOyxvgC+V0m7wTnSGxDFOXVTwS9tWHQBQ97ZjFSd0s0MbSKQO46M62Ll8jY
	dAqMBaw=
X-Google-Smtp-Source: AGHT+IF+5AJe4mKoP4NRGD4JhHKguUzRyAd0RbNOn7UJKNoaxTKdOnTypaODS9MqHy7Rr3Vgdzgdo+lFHc3r7C1dMw8=
X-Received: by 2002:a05:6902:13cf:b0:e93:3d4b:40d2 with SMTP id
 3f1490d57ef6-e951c2e654fmr21372131276.15.1756303105922; Wed, 27 Aug 2025
 06:58:25 -0700 (PDT)
MIME-Version: 1.0
References: <post-171945788@substack.com> <20250826121403.3.741fce49ca926be5@mg-d0.substack.com>
In-Reply-To: <20250826121403.3.741fce49ca926be5@mg-d0.substack.com>
From: Mykhaylo Kushnir <destifor@gmail.com>
Date: Wed, 27 Aug 2025 14:58:14 +0100
X-Gm-Features: Ac12FXypL6DsWSRzz7zCzi0flD-3_9cJFE9DXi02FeA2K_c_4oaCa8rxruJHVJ0
Message-ID: <CANPfs47Bpvr7z3tkGcMGMzjikUGH440cr0LWEP4iTRthxV2TZQ@mail.gmail.com>
Subject: Fwd: The Electric Slide
To: yevheniia.ilchenko@destilabs.com
Content-Type: multipart/alternative; boundary="000000000000bf1a7e063d592e8f"

--000000000000bf1a7e063d592e8f
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

---------- Forwarded message ---------
From: Not Boring <notboring@substack.com>
Date: Tue, Aug 26, 2025 at 1:15=E2=80=AFPM
Subject: The Electric Slide
To: <destifor@gmail.com>


The history, 99% decline, and future of the Electric Stack with Sam D'Amico
=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=
=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=
=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=
=CD=8F   =E2=80=87 =C2=AD=CD=8F
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =
=C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =
=E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD=CD=8F =
  =E2=80=87 =C2=AD=CD=8F   =E2=80=87 =C2=AD
Forwarded this email? Subscribe here
<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90Ym9yaW5nLmNvL3=
N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmc=
j1nZ3RhZiZuZXh0PWh0dHBzJTNBJTJGJTJGd3d3Lm5vdGJvcmluZy5jbyUyRnAlMkZ0aGUtZWxl=
Y3RyaWMtc2xpZGUiLCJwIjoxNzE5NDU3ODgsInMiOjEwMDI1LCJmIjp0cnVlLCJ1IjoyNzY1ODM=
xMSwiaWF0IjoxNzU2MjEwNTQ4LCJleHAiOjIwNzE3ODY1NDgsImlzcyI6InB1Yi0wIiwic3ViIj=
oibGluay1yZWRpcmVjdCJ9.YMuoo1FVToFVqlyU1TcnlqCs89xVp8IU91hZ4W5hPrA?>
for more
The Electric Slide
<https://substack.com/app-link/post?publication_id=3D10025&post_id=3D171945=
788&utm_source=3Dpost-email-title&utm_campaign=3Demail-post-title&isFreemai=
l=3Dtrue&r=3Dggtaf&token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1=
Nzg4LCJpYXQiOjE3NTYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicHViLTEwMDI1Iiw=
ic3ViIjoicG9zdC1yZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBSZJIu14HarD8>T=
he
history, 99% decline, and future of the Electric Stack with Sam D'Amico

Aug 26

<https://substack.com/app-link/post?publication_id=3D10025&post_id=3D171945=
788&utm_source=3Dsubstack&isFreemail=3Dtrue&submitLike=3Dtrue&token=3DeyJ1c=
2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJyZWFjdGlvbiI6IuKdpCIsImlh=
dCI6MTc1NjIxMDU0OCwiZXhwIjoxNzU4ODAyNTQ4LCJpc3MiOiJwdWItMTAwMjUiLCJzdWIiOiJ=
yZWFjdGlvbiJ9.hqQ2WkrFvp5wCoNoDb7STtUzx2XeVnb6NSneg5psw3E&utm_medium=3Demai=
l&utm_campaign=3Demail-reaction&r=3Dggtaf>
<https://substack.com/app-link/post?publication_id=3D10025&post_id=3D171945=
788&utm_source=3Dsubstack&utm_medium=3Demail&isFreemail=3Dtrue&comments=3Dt=
rue&token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJpYXQiOjE=
3NTYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicHViLTEwMDI1Iiwic3ViIjoicG9zdC=
1yZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBSZJIu14HarD8&r=3Dggtaf&utm_ca=
mpaign=3Demail-half-magic-comments&action=3Dpost-comment&utm_source=3Dsubst=
ack&utm_medium=3Demail>
<https://substack.com/app-link/post?publication_id=3D10025&post_id=3D171945=
788&utm_source=3Dsubstack&utm_medium=3Demail&utm_content=3Dshare&utm_campai=
gn=3Demail-share&action=3Dshare&triggerShare=3Dtrue&isFreemail=3Dtrue&r=3Dg=
gtaf&token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJpYXQiOj=
E3NTYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicHViLTEwMDI1Iiwic3ViIjoicG9zd=
C1yZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBSZJIu14HarD8>
<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS=
9wdWIvbm90Ym9yaW5nL3AvdGhlLWVsZWN0cmljLXNsaWRlP3V0bV9zb3VyY2U9c3Vic3RhY2smd=
XRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlv=
bj1yZXN0YWNrLWNvbW1lbnQmcj1nZ3RhZiZ0b2tlbj1leUoxYzJWeVgybGtJam95TnpZMU9ETXh=
NU3dpY0c5emRGOXBaQ0k2TVRjeE9UUTFOemc0TENKcFlYUWlPakUzTlRZeU1UQTFORGdzSW1WNG=
NDSTZNVGMxT0Rnd01qVTBPQ3dpYVhOeklqb2ljSFZpTFRFd01ESTFJaXdpYzNWaUlqb2ljRzl6Z=
EMxeVpXRmpkR2x2YmlKOS4wM0R1YnNDUHFBRFhrTE9XUElGZWI4NmJESGZfSUpCU1pKSXUxNEhh=
ckQ4IiwicCI6MTcxOTQ1Nzg4LCJzIjoxMDAyNSwiZiI6dHJ1ZSwidSI6Mjc2NTgzMTEsImlhdCI=
6MTc1NjIxMDU0OCwiZXhwIjoyMDcxNzg2NTQ4LCJpc3MiOiJwdWItMCIsInN1YiI6Imxpbmstcm=
VkaXJlY3QifQ.8rApQGF-8NftlJECt8_Vd3haFTpx7Yr2vFeHtSc02Oc?&utm_source=3Dsubs=
tack&utm_medium=3Demail>

READ IN APP
<https://open.substack.com/pub/notboring/p/the-electric-slide?utm_source=3D=
email&redirect=3Dapp-store&utm_campaign=3Demail-read-in-app>


*Welcome to the 1,269 newly Not Boring people who have joined us since our
last essay
<https://substack.com/redirect/f48ce800-2946-4373-af65-450ac49a09d2?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>!
Join 248,515 smart, curious folks by subscribing here: *
Subscribed
<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90Ym9yaW5nLmNvL2=
FjY291bnQiLCJwIjoxNzE5NDU3ODgsInMiOjEwMDI1LCJmIjp0cnVlLCJ1IjoyNzY1ODMxMSwia=
WF0IjoxNzU2MjEwNTQ4LCJleHAiOjIwNzE3ODY1NDgsImlzcyI6InB1Yi0wIiwic3ViIjoibGlu=
ay1yZWRpcmVjdCJ9.6EwrP_BnCp2ftrigPJd7gA_c3w2WR8Pbxgac0hw8HHI?>
------------------------------

Hi friends =F0=9F=91=8B ,

Happy Tuesday! Been a minute.

A month ago, I caught up with Sam D=E2=80=99Amico
<https://substack.com/redirect/7722923a-4bd3-4439-aff5-8f9806e1046d?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
the founder of Impulse Labs
<https://substack.com/redirect/4108f760-2361-4969-b567-16edac81f425?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>.
We got to talking, and decided to write something together on the modern
electric tech stack.

It would be simple, I thought: a few graphs showing how much the cost of
the stack has declined over the last few decades (99%, it turns out), a few
stories about demand for certain products driving those cost reductions,
bada bing, bada boom.

One month, over 100 hours of research and writing, and 40,000 words later,
it=E2=80=99s done.

Sam has been evangelizing the Electric Stack, and it=E2=80=99s resonating. =
Just
yesterday, Ryan McEntush at a16z published a great piece on the
Electro-Industrial
Stack
<https://substack.com/redirect/f7e940ac-8620-4c41-911d-75d6687ff32d?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
that discusses some of the topics we talk about here. We need more: that
there are hundreds of books, thousands of essays, and millions of tweets on
(and by) AI and so few on this topic is a reflection of American priorities
that will need to change.

This essay is my contribution to the conversation. It goes deep into the
history of the Electric Stack, introduces the Electric Slide
<https://substack.com/redirect/85b72f2b-b78f-433d-a06e-30ca7191d074?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
wrestles with the strategic logic of betting the future on AI, and ends
with cautious optimism about America=E2=80=99s ability to rebuild and win i=
n the
Electric Era.

If you want to jump straight to the online version: *Read The Electric
Slide Online
<https://substack.com/redirect/c70b44e2-b0f1-4826-bef6-90a6f061e51d?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*

If you want it as a PDF, you can download it here: *Electric Slide PDF
<https://substack.com/redirect/8633fa4e-b8a9-44d0-a9d7-88b43fbfd42b?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*

Let=E2=80=99s get to it.
------------------------------
*Today=E2=80=99s Not Boring is brought to you by=E2=80=A6 Vanta
<https://substack.com/redirect/0d28bb35-fda0-4750-a61a-f4411791453f?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*
<https://substack.com/redirect/0d28bb35-fda0-4750-a61a-f4411791453f?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>

*Vanta
<https://substack.com/redirect/0d28bb35-fda0-4750-a61a-f4411791453f?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
helps growing companies achieve compliance quickly and painlessly by
automating 35+ frameworks, including SOC 2, ISO 27001, HIPAA, and more.*

*Start with Vanta=E2=80=99s Compliance for Startups Bundle
<https://substack.com/redirect/0d28bb35-fda0-4750-a61a-f4411791453f?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
with key resources to accelerate your journey: step-by-step compliance
checklists, case studies from fast-growing startups, and on-demand videos
with industry leaders.*

*Get it here
<https://substack.com/redirect/0d28bb35-fda0-4750-a61a-f4411791453f?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>.*
------------------------------
The Electric Slide
<https://substack.com/redirect/04120d4c-243e-4b7c-93da-4ccfe804a348?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>

One of the more interesting developments in AI is that while the American
AI companies are mainly focused on closed-weight models, China is building
open-weight models
<https://substack.com/redirect/36fda68e-d995-42f2-adf4-d88d63a543fc?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
.

That begs the question: why?

On its face, the bet is simple: if China doesn=E2=80=99t have access to
leading-edge chips, then open-weights are the best way to encourage both
adoption and ecosystem development.

I think they=E2=80=99re making a different bet.

A couple of years ago, Isaiah Taylor
<https://substack.com/redirect/2cfcd8ac-374a-4c48-9835-58901df82243?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
the founder of nuclear company Valar Atomics
<https://substack.com/redirect/b1cff841-cacd-455e-945e-7e98f7494986?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
told me
<https://substack.com/redirect/ff3d9c7c-f10e-49b9-9503-2c1702d0e0c1?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
something that=E2=80=99s stuck in my head ever since:

*There are only really three pillars to anything around us, as far as
consumable goods. We've got energy, intelligence, and dexterity.*

I would generalize =E2=80=9Cdexterity=E2=80=9D to =E2=80=9Caction.=E2=80=9D=
 Everything we see around us,
and will see around us in the future, is the result of the potential to do
work (energy), the capacity to decide what to do and how (intelligence),
and the ability to manipulate matter (action).

In economic terms, energy, intelligence, and action are strong *complements=
*
in the production of anything.

And in the immortal words
<https://substack.com/redirect/fe6a2ca1-f3bb-475f-b0b8-94ee3ccc2e9f?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
of Joel Spolsky, *"Smart companies try to commoditize their products=E2=80=
=99
complements.=E2=80=9D*

America is, implicitly or explicitly, making a bet that whoever wins
intelligence, in the form of AI, wins the future.

*China is making a different bet: that for intelligence to truly matter, it
needs energy and action.*

If you control energy and action, making intelligence abundant strengthens
your position.

After catching up to America in electricity generation in just 2010, China
now generates 2.5x as much electricity as we do.
<https://substack.com/redirect/3f18314e-2e2a-439e-9b2b-9821ccbcb15a?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>

It also dominates the technologies that turn electricity into action: *the
Electric Stack*.

   -

   *Lithium-Ion Batteries*
   -

   *Magnets and Electric Motors*
   -

   *Power Electronics*
   -

   *Embedded Compute*

Today, China produces 75% of lithium-ion batteries globally and
manufactures 90% of the neodymium magnets that make motors spin. In power
electronics and embedded compute, it=E2=80=99s rapidly gaining ground.

That means that China controls the means of producing electric vehicles
(EVs), drones, robots, and all of the other electric products that are
replacing the combustion-driven machines on which America built its might.

As we speak, everything that moves, heats, lights up, computes, or converts
energy is being rebuilt to perform better, faster, cheaper, quieter, and as
a freebie, cleaner around electric technology.

*Simply put: anything that can go electric will.*

*Or rather, anything that can go electric **economically** will.*

Every year, the number of things that can economically go electric
increases as their components get cheaper and more performant. Every year,
China grows its Electric Stack capabilities relative to the West. Taken
together, that means that more of the physical cutting edge will be Made in
China.

And as humanity infuses machines with intelligence, more of those
intelligent machines will be Chinese.

This is why China is happy commoditizing AI. They believe that *action* is
the much harder, and therefore more valuable, piece of the future to own.

To understand why China is making this bet, and why they're probably right,
you need to understand what the Electric Stack is, how incredibly cheap
it's gotten, and who controls each layer.

The deeper you go, the more ridiculous it feels to believe that if we
simply build the best models, we will win economic and military dominance,
once you appreciate how all of this stuff works, how it all fits together.
You need to feel, in your bones, that research, great ideas, without the
manufacturing might to turn them into scaled products is no moat.

What follows is a surprisingly thrilling 40,000-word story of Western
invention and Eastern manufacturing, of GM selling our future for $70
million, of conferences in Pittsburgh and assembly lines in Fukushima, of
exactly how it is that drones fly, and of cost curves.

*The details matter because the details make the curve, and the curves are
destiny.*

Everyone reading this is likely familiar with Moore=E2=80=99s Law. Many of =
you are
likely familiar with scaling laws in AI, and Rich Sutton=E2=80=99s associat=
ed *Bitter
Lesson
<https://substack.com/redirect/986af27a-7f4e-410d-9c16-53d6b4b3996c?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*.
Somehow, as if by magic, these digital curves become self-fulfilling, their
audacity attracting talent and capital that make them come true.

These curves apply to the physical world, too.

We are all familiar with the solar panel cost curves
<https://substack.com/redirect/1a3904c3-76a1-4cad-8d9a-57ed8de8c03b?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
which have seen solar energy drop from $130.70 per watt in 1975 to $0.31
per watt today.
<https://substack.com/redirect/eada3419-f9d8-4fef-a115-8b8e65742143?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>

This has to do with electricity *generation*: turning some fuel =E2=80=93 o=
il,
coal, sunlight, wind, natural gas, uranium, or water - into electrons that
can be used to power practically anything.

We are less familiar with another set of curves: those that make up the
Electric Stack. These are the LEGO blocks that snap together to make the
products that *consume *electricity and turn it into action.

While there is a similar curve for batteries through 2018
<https://substack.com/redirect/4abe205d-d0c3-49fb-aae0-e8f423a599b3?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
there aren=E2=80=99t for the other layers of the Electric Stack, nor is the=
re one
Electric Stack curve. So we built them, in the hopes that they attract
people to build on the Electric Stack like Moore=E2=80=99s Law has attracte=
d people
to build on computers.

Each curve tells a story.

Since Sony started rolling out lithium-ion batteries in 1991, battery packs
have gotten 98.7% cheaper, for an annual decline of 12.5%.
<https://substack.com/redirect/808d47a9-3290-461b-a097-b08e8ab96a6f?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
*1991-2018:
Ziegler & Trancik MIT (adjusted to pack at 1.26x), 2019-2024: Bloomberg NEF=
*

Since hard-disk drive motors began incorporating Magnequench and Sumitomo
neodymium magnets in late 1980s, the cost of electromagnetic actuation has
dropped 98.8% from $204/kW to $5/kW, for an annual decline of 12.5%:=C2=B9
<https://substack.com/redirect/f94ce595-a52b-4d51-a0e0-51c660d6d7f7?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
*Source:
Catalogs, teardowns, government reports, you name it.*

Since industrial companies began using variable frequency drives (VFD)
using B. Jayant Baliga=E2=80=99s insulated gate bipolar transistors (IGBT) =
in the
late 1980s, VFD inverters have gotten 99.5% cheaper, for an annual decline
of 14.5%:
<https://substack.com/redirect/d026bebe-8c3c-4fb0-93e6-0c4e305658a8?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
*This
sources and methods note needs its whole own doc (linked)
<https://substack.com/redirect/0452e039-3350-458a-a472-5994483b6771?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*

And since Texas Instruments commercialized microcontrollers (MCUs) and
digital signal processors (DSPs) in calculators and kids toys in the late
1970s, the cost to run a million instructions per second (DMIPS) has fallen
99.9%, for an annual decline of 20% over the past 35 years:
<https://substack.com/redirect/97681631-62a4-4a3b-b621-0f0d632b6663?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
*This
one needs its own sources and methods doc, too (linked)
<https://substack.com/redirect/30a64782-712d-468c-b7a6-db0cb125d806?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*

To the best of our knowledge, no one has ever built a composite of these
curves: equally weight each component of the Electric Stack to understand
how much less it costs to build an electric product today than it did in
the past.

We built it, and we call it: *the Electric Slide
<https://substack.com/redirect/85b72f2b-b78f-433d-a06e-30ca7191d074?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>.*
<https://substack.com/redirect/ec4d3369-64e8-4b4a-a7be-f5cba0e0f9e5?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>

*It shows that the cost of the Electric Stack has fallen 99% since 1990, or
12.6% per year with an equal-weighted stack.*

No product=E2=80=99s bill of materials (BOM) actually has equally weighted
component costs, though, and no two BOMs are the same. A Tesla Model 3
might spend 60% of its BOM on batteries. A DJI Mavic 3 drone might devote
40% of its BOM to compute. So we cooked up an interactive Electric Slide
that you can *play with here
<https://substack.com/redirect/85b72f2b-b78f-433d-a06e-30ca7191d074?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*
:
<https://substack.com/redirect/5359f163-f268-46d5-a56e-9be55af76c7a?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>

*That today China owns two layers of the Electric Stack almost entirely was
not inevitable, or even likely*.

The four key Electric Stack technologies were invented at various points
between the 1960s and 1990s in America, Japan, and the UK, and reached
critical maturity around the same time in the 1990s.

Then, in many cases, we sold the future. GM sold its neo magnets division,
Magnequench, to China for $70 million. A123 Systems, which invented the
Lithium Iron Phosphate (LFP) battery, went bankrupt and sold to Wanxiang
for $257 million in 2013.

Thanks to shortsighted Western errors and farsighted Chinese industrial
policy, in the commercialization phase, the Electric Stack center of
gravity has moved from America and Japan to China, which dominates the
stack. By controlling these four technologies, China has become the world
leader in everything from EVs to drones to electric bikes to robots.

A giant piece of this is that mastery of this stack applies across domains,
allowing market leaders like BYD to make everything from cars, to home
energy products, to iPads, to much of the world=E2=80=99s drones. Within th=
e whole
sector =E2=80=93 the components, software, and expertise largely transfer =
=E2=80=93 meaning
mastery of one product of the stack allows success in scaling others.
Advantages compound. The result has been China getting the best =E2=80=9CLE=
GO set=E2=80=9D
in the world, with regards to this stack.

Conrad Bastable calls this LEGO set the *Electric Platform. *For a sobering
in-depth read on this topic, read his essay, *Forsaking Industrialism
<https://substack.com/redirect/f81adfa6-5ce7-4c59-a7a2-21d027252b93?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*.
This essay owes Conrad an enormous debt for both that piece, and the
conversation we had on Hyperlegible. I will reference both, explicitly or
implicitly, throughout.
<https://substack.com/redirect/81178af3-3880-42d2-a3bc-44e0770faba0?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>

Put another way, over the past half-century, the technologies in the
Electric Stack have gotten so cheap and so powerful that new entrants can
build better-performing products than incumbents. This is true for
companies - it=E2=80=99s a key enabler of my Vertical Integrators
<https://substack.com/redirect/3a5f62c6-ccfe-47bf-aefc-5215554ac966?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
thesis - and it=E2=80=99s also true for countries.

As the Electric Stack technologies ride down their learning curves, China
can better produce more of what the world wants.

Far from just making cheap components, its companies like BYD, DJI, and
Huawei, have put themselves among the world=E2=80=99s most innovative integ=
rators.
In Q4 2024, BYD passed Tesla in sales. Per the IEA
<https://substack.com/redirect/265015f2-1f0d-4265-8031-fe376351bcf0?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
=E2=80=9CChina continues to be the world=E2=80=99s EV manufacturing hub and=
 is responsible
for more than 70% of global production.=E2=80=9D

Conversely, America is systematically overemphasizing the role AI will play
in the future and underestimating the role that electrification will play.

As I wrote in *Base Chapter 2
<https://substack.com/redirect/621eca61-8dde-4195-b504-ff9fa2c6c231?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*:
=E2=80=9CWhile intelligence gets all of the attention, I=E2=80=99m increasi=
ngly convinced
that what we=E2=80=99re entering is the *Electric Era*. Cars, robots, flyin=
g cars,
drones, appliances, boats =E2=80=93 anything that can go electric is going
electric, because electric performs better. Even intelligence is reliant on
access to electricity.=E2=80=9D

*More broadly, America=E2=80=99s implicit stance is: we will specialize in
high-value creative work like software, chip design, and biotech research,
while other countries, mainly Taiwan and China, handle the low-margin
manufacturing. This is an outdated stance.*

Manufacturing and design are inextricably linked. When you make things, you
learn how to make them better. You learn which parts of the underlying
stack need to be improved, improve them, and make better products. This is
a theme that comes up over and over again in our Electric Stack story.

Texas Instruments won the Calculator Wars because it made its own
microcontrollers. Sony took lithium-ion batteries from bench-scale to mass
market scale and improved their efficiency by 50%. BYD made a lot of
batteries, then it started making cars, and the deep knowledge of both
allowed it to both bet on LFP early and develop the Blade Battery that it=
=E2=80=99s
ridden to EV dominance. Not for nothing, DeepSeek was able to basically
match OpenAI on less advanced chips because it went deeper into the guts
<https://substack.com/redirect/b901af0c-ab2d-4dfc-9be6-a8e7ea8cf4b0?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
of NVIDIA=E2=80=99s software than anyone else.

Ashlee Vance, who literally wrote the book on Elon Musk
<https://substack.com/redirect/584cc602-4078-409a-baca-859bc3b3264e?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
recently wrote that
<https://substack.com/redirect/4af58317-90c0-4884-aaeb-af5608ff6557?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
=E2=80=9CThe two biggest U.S. manufacturing success stories of the last twe=
nty
years are Tesla and SpaceX. And this is a problem.=E2=80=9D It is not surpr=
ising
that the person who sleeps on the factory floor and claims that the factory
is the product, not to mention the entrepreneur who most heartily embraced
vertical integration, is the one running both of those companies.

As we will see, the innovations that enabled the Model 3 came from a deep
knowledge of all of the components that make up a Tesla, and how they work
together. This same knowledge helped Tesla thrive through the COVID chip
shortage
<https://substack.com/redirect/1783d7a0-4304-4ae1-9d6a-082417ee0851?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
.

Even worse, though, and *if America=E2=80=99s advantage is in high-value cr=
eative
work, AI capable enough to confer economic and military supremacy packages
up and commoditizes that advantage.*

As I pointed out in my conversation with Conrad
<https://substack.com/redirect/8baa6778-e45c-4971-a2ad-d7af10b47339?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
=E2=80=9CIf you believe that America's advantage is the IP and the design a=
nd all
of that, the fact that we're racing to make that a commoditized good is
actually super ironic in a way that I hadn't appreciated before.=E2=80=9D

This, again, is why China is open sourcing intelligence.

Per Clayton Christensen=E2=80=99s Law of Conservation of Attractive Profits=
, if
intelligence becomes commoditized, profits will move to adjacent layers of
the value chain, like the electric product in which that intelligence
lives. A robot with a commoditized brain may capture more of the profits in
the value chain than the brains themselves, particularly if open source
models get good enough.

*To be blunt: in the Electric Era, maintaining design leadership without
manufacturing leadership is not a coherent strategic position, and one that
gets less coherent the better you believe AI will get.*

And the Electric Era is coming, because electric products are simply
better, and because they will keep getting better.

As part of my job, I get to see a little bit into the future, and from what
I see, electric products will win the coming decades.

A few months ago, I went for a ride in Arc=E2=80=99s
<https://substack.com/redirect/2165b3a2-62b1-4db0-8a0a-d794934bb550?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
electric boat, the ArcSport, on Lake Austin. It was faster,
sharper-turning, and quieter than any speedboat I=E2=80=99ve ever been on, =
and it
docked itself.

A few weeks ago, I went to Zipline=E2=80=99s
<https://substack.com/redirect/021d587f-0308-4265-b0ba-9e8839665e64?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
test site in California and watched, with my own eyes, as the drones held
perfect position thanks to electric motors that can adjust thrust hundreds
of times per second with perfect synchronization across multiple rotors,
enabled by precise power electronics and real-time compute.

MRI machines, like those used to detect cancer early
<https://substack.com/redirect/a0035c71-e136-4c91-a44d-2d3cb70c4581?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
depend entirely on powerful, precisely controlled electromagnets.
Residential batteries, like Base Power Company=E2=80=99s
<https://substack.com/redirect/2661e050-6465-4daa-8b6a-79b3bff768f8?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
can=E2=80=99t back up homes or balance the grid without the Electric Stack.=
 Robots,
whether modern industrial robots, surgical robots, Matic=E2=80=99s
<https://substack.com/redirect/b3ad077c-a02f-4a28-b114-8f54eba11af8?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
floor-cleaning robot, or futuristic humanoids, are made up of servomotors,
sophisticated power electronics, lithium batteries, and advanced compute.

These products all exist today. As the cost of Electric Stack continues to
decline and performance continues to improve, new products enter the
feasibility window.

Astro Mechanica
<https://substack.com/redirect/b17bb39d-bf55-422a-89ba-384e4b589aa1?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>
can build efficient supersonic planes, for example, because electric motors
have gotten powerful enough for their weight. Electric planes will begin to
make sense as batteries get more dense and motors more efficient. So too
will flying cars. And if we want affordable humanoid robots, even more than
smarter intelligence, we need better batteries, motors, inverters, and
microcontrollers.

*In fact, if we want AI to play a role in any of our physical products,
they need to be rebuilt on the Electric Stack first, so that they can speak
AI=E2=80=99s language.*

One of the reasons, I suspect, that America is so excited about AI and pays
relatively little attention to electrification (which, somehow, has been
politicized) is that the Electric Stack is messy. It exists in the real
world.

It is easy to imagine that a magical digital technology we don=E2=80=99t qu=
ite
understand but seem to be the best at will miraculously fix what ails us.
It is harder to imagine how in the world we might rebuild, and improve
upon, such an interconnected, physical stack of technologies, a stack that
has taken decades of research, luck, market forces, genius, and elbow
grease to get to this point, and one which China so thoroughly dominates.

The time for wishful thinking is over. There is a world to be rebuilt.

Whoever owns the Electric Stack owns the right to rebuild it in their image=
.

The learning curves are an incredibly useful guide: they tell us where
we=E2=80=99ve been, and more importantly, where we=E2=80=99re going.

But the curves are too smooth for real understanding. That smoothness masks
a ton of complexity: the research, the failures, the coincidences, the
business deals, the products, the industrial planning, and the ingenuity
that somehow, almost impossibly, came together to create the world we live
in.

So we will need to cover both, and we will need to go incredibly deep, so
you get a real feel for the thing, for the magnitude of both the miracle
and the challenge.

If America wants to win the future =E2=80=93 not because we=E2=80=99re itch=
ing for a fight,
but because we want to maintain our role as the world=E2=80=99s largest and=
 most
innovative economy =E2=80=93 we will need to vertically integrate. We need =
to have
the ability to manufacture every part of the Electric Stack, the
understanding of how to build the best products that comes from that
ability, and the ability to scale.

Getting this mojo back won=E2=80=99t be easy. It seems almost impossible. I=
t will
take industrial policy, innovation, government support, consumer demand,
and a little free market magic to pull it off. Currently, we are shooting
ourselves in the steel-toed foot.

One thing we=E2=80=99ll learn in studying the history is that demand for el=
ectric
products drives scale, cost declines, and performance improvements.

Unfortunately, electrification has become unnecessarily politicized in
America, with cultural associations obscuring the hard strategic realities.
While the current administration has shown understanding of electricity
generation through nuclear EOs and of component importance through
investments like the Pentagon=E2=80=99s $400 million in MP Materials
<https://substack.com/redirect/c19a8d3b-8862-4653-a6d6-96cd54a97521?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>,
the rollback of demand-side incentives undermines the very learning curves
that could restore American manufacturing dominance.

If I were President, I would make sure that every American man, woman, and
child has an EV, heat pump, drone, induction stove, and robot. American
demand is perhaps the most powerful motor in the world, and our best shot
at economically onshoring enough of the Electric Stack to remain
competitive in the Electric Era.

My hope is that by better understanding how we got here, we can avoid
mistakes like this and better determine where to go next.
*The Roadmap*

This is not a short essay, nor a light one, even by Not Boring=E2=80=99s st=
andards.
There are a few reasons for that.

First and foremost, given what I believe to be the importance of the
Electric Stack to the modern world and its future, we are woefully
unfamiliar with its history and details.

When I say =E2=80=9Cwe,=E2=80=9D I certainly mean me. As you might be able =
to tell, the
process of writing this essay involved a lot of =E2=80=9COH! *That=E2=80=99=
s* how that
works.=E2=80=9D Just as we hand-wave that AI will fix everything, we handwa=
ve about
the components of the Electric Stack based on a headline we read in the WSJ
or a tweet we scrolled by in our feed.

=E2=80=9CIt's critical that America not rely on China for batteries!=E2=80=
=9D Yes, but why,
and at which level should we integrate? =E2=80=9CChina controls 90% of rare=
 earth
magnet production!=E2=80=9D Yes, OK, but what is a rare earth magnet, what =
does it
do, why is it important that we manufacture them here, and how might we be
able to do that? I hope that by diving into an insane level of historical
detail, we can have more nuanced conversations about the future.

Second, because I find this stuff fascinating. The tale is full of hidden
legends and business case studies - triumphs and fumbles - that shape how
the world moves.

Any hope of getting our efforts right this time requires an understanding
of where they=E2=80=99ve gone wrong (or right) in the past.

Finally, because the curves themselves tell stories, predict the future,
and in so doing, bring that future into existence.

The components that make up modern electric products have gotten so cheap
and so performant that entirely new things are becoming possible and
economical each year. And while they *feel* less likely to continue because
they have to interact with the physical world, somehow, they do. People
keep underestimating how cheap solar is going to be; the same should be
true for most things built on the Electric Stack.

That=E2=80=99s another reason to write the stories in addition to simply sh=
owing
the curves. Every story shows a technological tree that seems to have hit
its last branch, before someone, somewhere tries a new chemistry, adds a
new element, or configures the LEGO blocks in just such a way that,
suddenly, it just kind of works, works enough, at least, for a specific
product that really needs it to work just that way=E2=80=A6 and the rest is
history. The curves continue.

There=E2=80=99s a risk in an essay like this of painting one of two picture=
s:
either that we must do everything in our power to beat China or that we are
so hopelessly behind that there=E2=80=99s no point, that we should just foc=
us on
the game we can win, even if it=E2=80=99s not the most important game.

I think the curves tell an optimistic story: that, thanks in large part to
Western science and Eastern manufacturing, these technologies have now
reached a point at which it is becoming increasingly possible to build an
Electric world, economically.

This is a long piece, but it=E2=80=99s one that I=E2=80=99ve loved research=
ing and writing
over the past month, and I think it=E2=80=99s the most comprehensive resour=
ce for
those who want to understand how we got here and where we might go in the
Electric Era.

We will cover:

   1.

   *A Brief History of Electromagnetism:* The force driving the Electric
   Era.
   2.

   *How Electric Motors Work: *Establishing the fundamentals.
   3.

   *Lithium-Ion Batteries: *Li-Ion, NMC, NCA, Tesla, BYD, CATL, and LFP.
   4.

   *Magnets and Electric Motors: *the neodymium magnets that spin the world=
.
   5.

   *The Century of Semiconductors: *the birth of compute.
   6.

   *Power Electronics and Control Systems:* controlling electricity with
   itself.
   7.

   *Embedded Compute: *microcontrollers, DSPs, ARM, and RISC-V.
   8.

   *Lessons and Takeaways: *What can we learn from the history of the
   Electric Stack?
   9.

   *Rebuilding the Electric Stack: *What it will take to build the future.

To be clear upfront: rebuilding the Electric Stack in the West will be
hard, but possible. America still owns the greatest demand and
entrepreneurial engines the world has ever seen. We will need to run both
at about a million RPMs.

So without further ado, let=E2=80=99s begin. And we must begin, of course, =
all the
way at the bottom, with some fundamental physics.
------------------------------

To read the full essay online: *Read The Electric Slide Online
<https://substack.com/redirect/c70b44e2-b0f1-4826-bef6-90a6f061e51d?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*

If you want it as a PDF, you can download it here: *Electric Slide PDF
<https://substack.com/redirect/8633fa4e-b8a9-44d0-a9d7-88b43fbfd42b?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>*
------------------------------

*Huge thanks to Sam D=E2=80=99Amico for working on this monster with me, an=
d to
Conrad Bastable for many of the original ideas! Everyone go buy an Impulse
stove
<https://substack.com/redirect/4108f760-2361-4969-b567-16edac81f425?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>.
*
------------------------------

That=E2=80=99s all for today. We=E2=80=99ll be back in your inbox on Friday=
 with a Weekly
Dose.

Thanks for reading,

Packy
1

You have no idea how hard it was to find this data. It doesn=E2=80=99t exis=
t in one
place. It=E2=80=99s everywhere, in old catalogs, YouTube teardowns, governm=
ent
reports. The data isn=E2=80=99t clean: old hard-disk drives have higher $/k=
W in
part because they needed so few kilowatts; the denominator was very high.
Comparing that to a modern EV motor feels a little absurd, but it=E2=80=99s=
 also
how the progress actually happened, so we=E2=80=99re sticking with it. We u=
sed
Claude and ChatGPT to help find all of the data, and you can find a list of
sources here
<https://substack.com/redirect/7a8af3ed-1740-4c22-abd3-efd894ca62cf?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>.
This graph does its best to normalize across and account for a bunch of
different industries that use electromagnetic motors, although in some
cases, certain use cases achieved better $/kW performance. The Tesla Model
3, for example, got below $5/kW. It is directionally correct, and while
specific years may be off the takeaway is the same: 98.8% reduction in the
past 35 years.

A guest post by
Sam D'Amico
<https://substack.com/@derp?utm_campaign=3Dguest_post_bio&utm_medium=3Demai=
l>
Subscribe
<https://substack.com/redirect/be7b02da-6563-47ba-8d7d-83f9318bade2?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>

Share
<https://substack.com/app-link/post?publication_id=3D10025&post_id=3D171945=
788&utm_source=3Dsubstack&utm_medium=3Demail&utm_content=3Dshare&utm_campai=
gn=3Demail-share&action=3Dshare&triggerShare=3Dtrue&isFreemail=3Dtrue&r=3Dg=
gtaf&token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJpYXQiOj=
E3NTYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicHViLTEwMDI1Iiwic3ViIjoicG9zd=
C1yZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBSZJIu14HarD8>


Like
<https://substack.com/app-link/post?publication_id=3D10025&post_id=3D171945=
788&utm_source=3Dsubstack&isFreemail=3Dtrue&submitLike=3Dtrue&token=3DeyJ1c=
2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJyZWFjdGlvbiI6IuKdpCIsImlh=
dCI6MTc1NjIxMDU0OCwiZXhwIjoxNzU4ODAyNTQ4LCJpc3MiOiJwdWItMTAwMjUiLCJzdWIiOiJ=
yZWFjdGlvbiJ9.hqQ2WkrFvp5wCoNoDb7STtUzx2XeVnb6NSneg5psw3E&utm_medium=3Demai=
l&utm_campaign=3Demail-reaction&r=3Dggtaf>
Comment
<https://substack.com/app-link/post?publication_id=3D10025&post_id=3D171945=
788&utm_source=3Dsubstack&utm_medium=3Demail&isFreemail=3Dtrue&comments=3Dt=
rue&token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJpYXQiOjE=
3NTYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicHViLTEwMDI1Iiwic3ViIjoicG9zdC=
1yZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBSZJIu14HarD8&r=3Dggtaf&utm_ca=
mpaign=3Demail-half-magic-comments&action=3Dpost-comment&utm_source=3Dsubst=
ack&utm_medium=3Demail>
Restack
<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS=
9wdWIvbm90Ym9yaW5nL3AvdGhlLWVsZWN0cmljLXNsaWRlP3V0bV9zb3VyY2U9c3Vic3RhY2smd=
XRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlv=
bj1yZXN0YWNrLWNvbW1lbnQmcj1nZ3RhZiZ0b2tlbj1leUoxYzJWeVgybGtJam95TnpZMU9ETXh=
NU3dpY0c5emRGOXBaQ0k2TVRjeE9UUTFOemc0TENKcFlYUWlPakUzTlRZeU1UQTFORGdzSW1WNG=
NDSTZNVGMxT0Rnd01qVTBPQ3dpYVhOeklqb2ljSFZpTFRFd01ESTFJaXdpYzNWaUlqb2ljRzl6Z=
EMxeVpXRmpkR2x2YmlKOS4wM0R1YnNDUHFBRFhrTE9XUElGZWI4NmJESGZfSUpCU1pKSXUxNEhh=
ckQ4IiwicCI6MTcxOTQ1Nzg4LCJzIjoxMDAyNSwiZiI6dHJ1ZSwidSI6Mjc2NTgzMTEsImlhdCI=
6MTc1NjIxMDU0OCwiZXhwIjoyMDcxNzg2NTQ4LCJpc3MiOiJwdWItMCIsInN1YiI6Imxpbmstcm=
VkaXJlY3QifQ.8rApQGF-8NftlJECt8_Vd3haFTpx7Yr2vFeHtSc02Oc?&utm_source=3Dsubs=
tack&utm_medium=3Demail>


=C2=A9 2025 Packy McCormick
Brooklyn, NY
Unsubscribe
<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90Ym9yaW5nLmNvL2=
FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOelkxT0RNeE1Td2ljR=
zl6ZEY5cFpDSTZNVGN4T1RRMU56ZzRMQ0pwWVhRaU9qRTNOVFl5TVRBMU5EZ3NJbVY0Y0NJNk1U=
YzROemMwTmpVME9Dd2lhWE56SWpvaWNIVmlMVEV3TURJMUlpd2ljM1ZpSWpvaVpHbHpZV0pzWlY=
5bGJXRnBiQ0o5Li1PMHFhQUJJLVg0d20xY2tzOW1SdU1qVEpnNEZ4b280eHVHSmdQQl9mZnMiLC=
JwIjoxNzE5NDU3ODgsInMiOjEwMDI1LCJmIjp0cnVlLCJ1IjoyNzY1ODMxMSwiaWF0IjoxNzU2M=
jEwNTQ4LCJleHAiOjIwNzE3ODY1NDgsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVj=
dCJ9.4_kE8TeFNId3wpycnUcOSiVQd-26fI9-o9bAVK7PW6o?>

[image: Get the app]
<https://substack.com/redirect/35c6b1d1-7dca-4979-ba6c-a8dd083ead95?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc>[image:
Start writing]
<https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbn=
VwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290Z=
XImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD1kZXN0aWZv=
ckBnbWFpbC5jb20mcj1nZ3RhZiIsInAiOjE3MTk0NTc4OCwicyI6MTAwMjUsImYiOnRydWUsInU=
iOjI3NjU4MzExLCJpYXQiOjE3NTYyMTA1NDgsImV4cCI6MjA3MTc4NjU0OCwiaXNzIjoicHViLT=
AiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.sUOubxcRlTqQoG1WVp7ovlgNPeLa9V-4KSgY0Kn80=
Pc?>

--000000000000bf1a7e063d592e8f
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr"><br><br><div class=3D"gmail_quote gmail_quote_container"><=
div dir=3D"ltr" class=3D"gmail_attr">---------- Forwarded message ---------=
<br>From: <strong class=3D"gmail_sendername" dir=3D"auto">Not Boring</stron=
g> <span dir=3D"auto">&lt;<a href=3D"mailto:notboring@substack.com">notbori=
ng@substack.com</a>&gt;</span><br>Date: Tue, Aug 26, 2025 at 1:15=E2=80=AFP=
M<br>Subject: The Electric Slide<br>To:  &lt;<a href=3D"mailto:destifor@gma=
il.com">destifor@gmail.com</a>&gt;<br></div><br><br><div style=3D"font-kern=
ing:auto"><img src=3D"https://eotrx.substackcdn.com/open?token=3DeyJtIjoiPD=
IwMjUwODI2MTIxNDAzLjMuNzQxZmNlNDljYTkyNmJlNUBtZy1kMC5zdWJzdGFjay5jb20-Iiwid=
SI6Mjc2NTgzMTEsInIiOiJkZXN0aWZvckBnbWFpbC5jb20iLCJkIjoibWctZDAuc3Vic3RhY2su=
Y29tIiwicCI6MTcxOTQ1Nzg4LCJ0IjoibmV3c2xldHRlciIsImEiOiJldmVyeW9uZSIsInMiOjE=
wMDI1LCJjIjoicG9zdCIsImYiOnRydWUsInBvc2l0aW9uIjoidG9wIiwiaWF0IjoxNzU2MjEwNT=
Q5LCJleHAiOjE3NTg4MDI1NDksImlzcyI6InB1Yi0wIiwic3ViIjoiZW8ifQ.MnM9_F1GfGuGGd=
o_lIfh6qEAL4BTTNs1qdqkn7mc6bY" alt=3D"" width=3D"1" height=3D"1" border=3D"=
0" style=3D"height:1px!important;width:1px!important;border-width:0!importa=
nt;margin-top:0!important;margin-bottom:0!important;margin-right:0!importan=
t;margin-left:0!important;padding-top:0!important;padding-bottom:0!importan=
t;padding-right:0!important;padding-left:0!important"><div style=3D"display=
:none;font-size:1px;color:#333333;line-height:1px;max-height:0px;max-width:=
0px;opacity:0;overflow:hidden">The history, 99% decline, and future of the =
Electric Stack with Sam D&#39;Amico</div><div style=3D"display:none;font-si=
ze:1px;color:#333333;line-height:1px;max-height:0px;max-width:0px;opacity:0=
;overflow:hidden">=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=
=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =
=C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =
=C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=
=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=
=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=
=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=
=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =
=E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=AD=CD=8F =C2=A0 =E2=80=87 =C2=
=AD</div><table role=3D"presentation" width=3D"100%" border=3D"0" cellspaci=
ng=3D"0" cellpadding=3D"0"><tbody><tr><td></td><td width=3D"550"></td><td><=
/td></tr><tr><td></td><td width=3D"550" align=3D"left"><div style=3D"font-s=
ize:16px;line-height:26px;max-width:550px;width:100%;margin:0 auto"><table =
role=3D"presentation" width=3D"100%" border=3D"0" cellspacing=3D"0" cellpad=
ding=3D"0"><tbody><tr><td align=3D"right" style=3D"height:20px"><table role=
=3D"presentation" width=3D"auto" border=3D"0" cellspacing=3D"0" cellpadding=
=3D"0"><tbody><tr><td style=3D"vertical-align:middle"><span style=3D"font-f=
amily:SF Pro Text,-apple-system,system-ui,BlinkMacSystemFont,Inter,Segoe UI=
,Roboto,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe U=
I Symbol;font-size:13px;color:unset;list-style:none;text-decoration:unset;m=
argin:0"><div style=3D"list-style:none;color:unset;text-align:right;font-si=
ze:12px;line-height:16px;text-decoration:unset;margin:0"><span style=3D"lis=
t-style:none;color:unset;text-decoration:unset;margin:0">Forwarded this ema=
il? <a href=3D"https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90=
Ym9yaW5nLmNvL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1=
zdWJzY3JpYmUmcj1nZ3RhZiZuZXh0PWh0dHBzJTNBJTJGJTJGd3d3Lm5vdGJvcmluZy5jbyUyRn=
AlMkZ0aGUtZWxlY3RyaWMtc2xpZGUiLCJwIjoxNzE5NDU3ODgsInMiOjEwMDI1LCJmIjp0cnVlL=
CJ1IjoyNzY1ODMxMSwiaWF0IjoxNzU2MjEwNTQ4LCJleHAiOjIwNzE3ODY1NDgsImlzcyI6InB1=
Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.YMuoo1FVToFVqlyU1TcnlqCs89xVp8IU91hZ4W=
5hPrA?" style=3D"list-style:none;color:unset;text-decoration:unset;margin:0=
;text-decoration-line:underline" target=3D"_blank">Subscribe here</a> for m=
ore</span></div></span></td></tr></tbody></table></td></tr></tbody></table>=
<div dir=3D"auto" style=3D"padding:32px 0 0 0;font-size:16px;line-height:26=
px"><div role=3D"region" aria-label=3D"Post header" style=3D"font-size:16px=
;line-height:26px"><h1 dir=3D"auto" style=3D"direction:auto;text-align:star=
t;unicode-bidi:isolate;color:rgb(54,55,55);font-family:Lora,sans-serif;font=
-weight:600;margin:0;line-height:36px;font-size:32px"><a href=3D"https://su=
bstack.com/app-link/post?publication_id=3D10025&amp;post_id=3D171945788&amp=
;utm_source=3Dpost-email-title&amp;utm_campaign=3Demail-post-title&amp;isFr=
eemail=3Dtrue&amp;r=3Dggtaf&amp;token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9=
pZCI6MTcxOTQ1Nzg4LCJpYXQiOjE3NTYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicH=
ViLTEwMDI1Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBS=
ZJIu14HarD8" style=3D"color:rgb(54,55,55);text-decoration:none" target=3D"_=
blank">The Electric Slide</a></h1><h3 dir=3D"auto" style=3D"direction:auto;=
text-align:start;unicode-bidi:isolate;font-family:&#39;SF Pro Display&#39;,=
-apple-system-headline,system-ui,-apple-system,BlinkMacSystemFont,&#39;Sego=
e UI&#39;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#3=
9;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;font-weight:normal;margin:4=
px 0 0;color:#777777;line-height:24px;font-size:18px;margin-top:12px">The h=
istory, 99% decline, and future of the Electric Stack with Sam D&#39;Amico<=
/h3><table cellpadding=3D"0" cellspacing=3D"0" style=3D"margin:1em 0;height=
:20px"><tbody><tr><td title=3D"2025-08-26T12:14:11.178Z" style=3D"padding:0=
px 12px 0px 0;height:14px;font-size:14px;font-family:system-ui,-apple-syste=
m,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,sans-serif,&=
#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#3=
9;;color:#777777;text-decoration:none;margin-right:0;padding-right:0;white-=
space:nowrap;font-weight:400;padding-top:0;padding-bottom:0"><div style=3D"=
list-style:none;font-size:11px;line-height:20px;text-decoration:unset;color=
:rgb(119,119,119);margin:0;font-family:&#39;SF Compact&#39;,-apple-system,s=
ystem-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helveti=
ca,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#=
39;Segoe UI Symbol&#39;;font-weight:500;text-transform:uppercase;letter-spa=
cing:.2px">Aug 26</div></td></tr></tbody></table><table role=3D"presentatio=
n" width=3D"100%" border=3D"0" cellspacing=3D"0" cellpadding=3D"0" style=3D=
"border-top:1px solid rgb(0,0,0,.1);border-bottom:1px solid rgb(0,0,0,.1);m=
in-width:100%"><tbody><tr height=3D"16"><td height=3D"16" style=3D"font-siz=
e:0px;line-height:0">=C2=A0</td></tr><tr><td><table role=3D"presentation" w=
idth=3D"100%" border=3D"0" cellspacing=3D"0" cellpadding=3D"0"><tbody><tr><=
td><table role=3D"presentation" width=3D"auto" border=3D"0" cellspacing=3D"=
0" cellpadding=3D"0"><tbody><tr><td style=3D"vertical-align:middle"><table =
role=3D"presentation" width=3D"38" border=3D"0" cellspacing=3D"0" cellpaddi=
ng=3D"0"><tbody><tr><td align=3D"center"><a href=3D"https://substack.com/ap=
p-link/post?publication_id=3D10025&amp;post_id=3D171945788&amp;utm_source=
=3Dsubstack&amp;isFreemail=3Dtrue&amp;submitLike=3Dtrue&amp;token=3DeyJ1c2V=
yX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJyZWFjdGlvbiI6IuKdpCIsImlhdC=
I6MTc1NjIxMDU0OCwiZXhwIjoxNzU4ODAyNTQ4LCJpc3MiOiJwdWItMTAwMjUiLCJzdWIiOiJyZ=
WFjdGlvbiJ9.hqQ2WkrFvp5wCoNoDb7STtUzx2XeVnb6NSneg5psw3E&amp;utm_medium=3Dem=
ail&amp;utm_campaign=3Demail-reaction&amp;r=3Dggtaf" style=3D"font-family:s=
ystem-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helveti=
ca,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#=
39;Segoe UI Symbol&#39;;display:inline-block;font-weight:500;border:1px sol=
id rgb(0,0,0,.1);border-radius:9999px;text-transform:uppercase;font-size:12=
px;line-height:1;padding:9px 0;text-decoration:none;color:rgb(119,119,119);=
min-width:38px;box-sizing:border-box;width:38px" target=3D"_blank"><img src=
=3D"https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto=
:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%=
3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D=
2" width=3D"18" height=3D"18" style=3D"border:none;vertical-align:middle;ma=
x-width:18px" alt=3D""></a></td></tr></tbody></table></td><td width=3D"8" s=
tyle=3D"min-width:8px"></td><td style=3D"vertical-align:middle"><table role=
=3D"presentation" width=3D"38" border=3D"0" cellspacing=3D"0" cellpadding=
=3D"0"><tbody><tr><td align=3D"center"><a href=3D"https://substack.com/app-=
link/post?publication_id=3D10025&amp;post_id=3D171945788&amp;utm_source=3Ds=
ubstack&amp;utm_medium=3Demail&amp;isFreemail=3Dtrue&amp;comments=3Dtrue&am=
p;token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJpYXQiOjE3N=
TYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicHViLTEwMDI1Iiwic3ViIjoicG9zdC1y=
ZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBSZJIu14HarD8&amp;r=3Dggtaf&amp;=
utm_campaign=3Demail-half-magic-comments&amp;action=3Dpost-comment&amp;utm_=
source=3Dsubstack&amp;utm_medium=3Demail" style=3D"font-family:system-ui,-a=
pple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,sa=
ns-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI=
 Symbol&#39;;display:inline-block;font-weight:500;border:1px solid rgb(0,0,=
0,.1);border-radius:9999px;text-transform:uppercase;font-size:12px;line-hei=
ght:1;padding:9px 0;text-decoration:none;color:rgb(119,119,119);min-width:3=
8px;box-sizing:border-box;width:38px" target=3D"_blank"><img src=3D"https:/=
/substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_pr=
ogressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%=
26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2" width=
=3D"18" height=3D"18" style=3D"border:none;vertical-align:middle;max-width:=
18px" alt=3D""></a></td></tr></tbody></table></td><td width=3D"8" style=3D"=
min-width:8px"></td><td style=3D"vertical-align:middle"><table role=3D"pres=
entation" width=3D"38" border=3D"0" cellspacing=3D"0" cellpadding=3D"0"><tb=
ody><tr><td align=3D"center"><a href=3D"https://substack.com/app-link/post?=
publication_id=3D10025&amp;post_id=3D171945788&amp;utm_source=3Dsubstack&am=
p;utm_medium=3Demail&amp;utm_content=3Dshare&amp;utm_campaign=3Demail-share=
&amp;action=3Dshare&amp;triggerShare=3Dtrue&amp;isFreemail=3Dtrue&amp;r=3Dg=
gtaf&amp;token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJpYX=
QiOjE3NTYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicHViLTEwMDI1Iiwic3ViIjoic=
G9zdC1yZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBSZJIu14HarD8" style=3D"f=
ont-family:system-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Ro=
boto,Helvetica,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI E=
moji&#39;,&#39;Segoe UI Symbol&#39;;display:inline-block;font-weight:500;bo=
rder:1px solid rgb(0,0,0,.1);border-radius:9999px;text-transform:uppercase;=
font-size:12px;line-height:1;padding:9px 0;text-decoration:none;color:rgb(1=
19,119,119);min-width:38px;box-sizing:border-box;width:38px" target=3D"_bla=
nk"><img src=3D"https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,=
f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2F=
LucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26s=
trokeWidth%3D2" width=3D"18" height=3D"18" style=3D"border:none;vertical-al=
ign:middle;max-width:18px" alt=3D""></a></td></tr></tbody></table></td><td =
width=3D"8" style=3D"min-width:8px"></td><td style=3D"vertical-align:middle=
"><table role=3D"presentation" width=3D"38" border=3D"0" cellspacing=3D"0" =
cellpadding=3D"0"><tbody><tr><td align=3D"center"><a href=3D"https://substa=
ck.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvbm90Ym9ya=
W5nL3AvdGhlLWVsZWN0cmljLXNsaWRlP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1l=
bWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWN=
vbW1lbnQmcj1nZ3RhZiZ0b2tlbj1leUoxYzJWeVgybGtJam95TnpZMU9ETXhNU3dpY0c5emRGOX=
BaQ0k2TVRjeE9UUTFOemc0TENKcFlYUWlPakUzTlRZeU1UQTFORGdzSW1WNGNDSTZNVGMxT0Rnd=
01qVTBPQ3dpYVhOeklqb2ljSFZpTFRFd01ESTFJaXdpYzNWaUlqb2ljRzl6ZEMxeVpXRmpkR2x2=
YmlKOS4wM0R1YnNDUHFBRFhrTE9XUElGZWI4NmJESGZfSUpCU1pKSXUxNEhhckQ4IiwicCI6MTc=
xOTQ1Nzg4LCJzIjoxMDAyNSwiZiI6dHJ1ZSwidSI6Mjc2NTgzMTEsImlhdCI6MTc1NjIxMDU0OC=
wiZXhwIjoyMDcxNzg2NTQ4LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.8r=
ApQGF-8NftlJECt8_Vd3haFTpx7Yr2vFeHtSc02Oc?&amp;utm_source=3Dsubstack&amp;ut=
m_medium=3Demail" style=3D"font-family:system-ui,-apple-system,BlinkMacSyst=
emFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Colo=
r Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;display:inl=
ine-block;font-weight:500;border:1px solid rgb(0,0,0,.1);border-radius:9999=
px;text-transform:uppercase;font-size:12px;line-height:1;padding:9px 0;text=
-decoration:none;color:rgb(119,119,119);min-width:38px;box-sizing:border-bo=
x;width:38px" target=3D"_blank"><img src=3D"https://substackcdn.com/image/f=
etch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A=
%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3D=
none%26stroke%3D%2523808080%26strokeWidth%3D2" width=3D"18" height=3D"18" s=
tyle=3D"border:none;vertical-align:middle;max-width:18px" alt=3D""></a></td=
></tr></tbody></table></td></tr></tbody></table></td><td align=3D"right"><t=
able role=3D"presentation" width=3D"auto" border=3D"0" cellspacing=3D"0" ce=
llpadding=3D"0"><tbody><tr><td style=3D"vertical-align:middle"><table role=
=3D"presentation" width=3D"auto" border=3D"0" cellspacing=3D"0" cellpadding=
=3D"0"><tbody><tr><td align=3D"center"><a href=3D"https://open.substack.com=
/pub/notboring/p/the-electric-slide?utm_source=3Demail&amp;redirect=3Dapp-s=
tore&amp;utm_campaign=3Demail-read-in-app" style=3D"font-family:system-ui,-=
apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,s=
ans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe U=
I Symbol&#39;;display:inline-block;font-weight:500;border:1px solid rgb(0,0=
,0,.1);border-radius:9999px;text-transform:uppercase;font-size:12px;line-he=
ight:12px;padding:9px 14px;text-decoration:none;color:rgb(119,119,119)" tar=
get=3D"_blank"><div style=3D"font-size:16px;line-height:26px;display:inline=
-block;vertical-align:middle;max-width:0;min-height:18px"></div><span style=
=3D"vertical-align:middle;margin-right:4px">READ IN APP</span><img src=3D"h=
ttps://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good=
,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRigh=
t%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%=
3D2" width=3D"18" height=3D"18" style=3D"min-width:18px;min-height:18px;bor=
der:none;vertical-align:middle;margin-right:0;margin-left:0;max-width:18px"=
 alt=3D""></a></td></tr></tbody></table></td></tr></tbody></table></td></tr=
></tbody></table></td></tr><tr height=3D"16"><td height=3D"16" style=3D"fon=
t-size:0px;line-height:0">=C2=A0</td></tr></tbody></table></div></div><div =
dir=3D"auto" style=3D"padding:32px 0 0 0;font-size:16px;line-height:26px"><=
div dir=3D"auto" style=3D"text-align:initial;font-size:16px;line-height:26p=
x;width:100%;word-break:break-word;margin-bottom:16px"><p style=3D"margin:0=
 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px;margin-top:0"=
><em><span>Welcome to the </span><strong>1,269 newly Not Boring people</str=
ong><span> who have joined us since our </span><a href=3D"https://substack.=
com/redirect/f48ce800-2946-4373-af65-450ac49a09d2?j=3DeyJ1IjoiZ2d0YWYifQ.AR=
MsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,5=
5,55);text-decoration:underline" target=3D"_blank">last essay</a><span>! Jo=
in</span><strong> 248,515</strong><span> smart, curious folks by subscribin=
g here: </span></em></p><div style=3D"margin:0 0 1em;direction:ltr;font-siz=
e:16px;line-height:26px"><div style=3D"text-decoration:unset;list-style:non=
e;font-size:16px;line-height:26px;text-align:center;border-radius:4px"><a h=
ref=3D"https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90Ym9yaW5n=
LmNvL2FjY291bnQiLCJwIjoxNzE5NDU3ODgsInMiOjEwMDI1LCJmIjp0cnVlLCJ1IjoyNzY1ODM=
xMSwiaWF0IjoxNzU2MjEwNTQ4LCJleHAiOjIwNzE3ODY1NDgsImlzcyI6InB1Yi0wIiwic3ViIj=
oibGluay1yZWRpcmVjdCJ9.6EwrP_BnCp2ftrigPJd7gA_c3w2WR8Pbxgac0hw8HHI?" style=
=3D"font-family:system-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#3=
9;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe=
 UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;display:inline-block;box-sizing:bo=
rder-box;border-radius:8px;font-size:14px;line-height:20px;font-weight:600;=
text-align:center;background-color:transparent;opacity:1;outline:none;white=
-space:nowrap;text-decoration:none!important;border:1px solid #0c2427;margi=
n:0 auto;background:transparent;color:#0c2427;padding:12px 20px;height:auto=
" target=3D"_blank"><img src=3D"https://substackcdn.com/image/fetch/$s_!Pcy=
E!,w_40,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubsta=
ck.com%2Ficon%2FLucideCheck%3Fv%3D4%26height%3D40%26fill%3Dtransparent%26st=
roke%3D%25230c2427%26strokeWidth%3D3.6" width=3D"20" height=3D"20" style=3D=
"border:none;vertical-align:middle;height:auto;display:inline-block;max-wid=
th:20px" alt=3D""><span style=3D"text-decoration:none">Subscribed</span></a=
></div></div><div style=3D"font-size:16px;line-height:26px"><hr style=3D"ma=
rgin:32px 0;padding:0;height:1px;background:#e6e6e6;border:none"></div><p s=
tyle=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16=
px">Hi friends =F0=9F=91=8B ,</p><p style=3D"margin:0 0 20px 0;color:rgb(54=
,55,55);line-height:26px;font-size:16px">Happy Tuesday! Been a minute. </p>=
<p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-siz=
e:16px"><span>A month ago, I caught up with </span><a href=3D"https://subst=
ack.com/redirect/7722923a-4bd3-4439-aff5-8f9806e1046d?j=3DeyJ1IjoiZ2d0YWYif=
Q.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(=
54,55,55);text-decoration:underline" target=3D"_blank">Sam D=E2=80=99Amico<=
/a><span>, the founder of </span><a href=3D"https://substack.com/redirect/4=
108f760-2361-4969-b567-16edac81f425?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZ=
Y74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-dec=
oration:underline" target=3D"_blank">Impulse Labs</a><span>. We got to talk=
ing, and decided to write something together on the modern electric tech st=
ack.</span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-heigh=
t:26px;font-size:16px">It would be simple, I thought: a few graphs showing =
how much the cost of the stack has declined over the last few decades (99%,=
 it turns out), a few stories about demand for certain products driving tho=
se cost reductions, bada bing, bada boom.</p><p style=3D"margin:0 0 20px 0;=
color:rgb(54,55,55);line-height:26px;font-size:16px">One month, over 100 ho=
urs of research and writing, and 40,000 words later, it=E2=80=99s done. </p=
><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-si=
ze:16px"><span>Sam has been evangelizing the Electric Stack, and it=E2=80=
=99s resonating. Just yesterday, Ryan McEntush at a16z published a great pi=
ece on the </span><a href=3D"https://substack.com/redirect/f7e940ac-8620-4c=
41-911d-75d6687ff32d?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74Uo=
gZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:underli=
ne" target=3D"_blank">Electro-Industrial Stack</a><span> that discusses som=
e of the topics we talk about here. We need more: that there are hundreds o=
f books, thousands of essays, and millions of tweets on (and by) AI and so =
few on this topic is a reflection of American priorities that will need to =
change. </span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-h=
eight:26px;font-size:16px"><span>This essay is my contribution to the conve=
rsation. It goes deep into the history of the Electric Stack, introduces th=
e </span><a href=3D"https://substack.com/redirect/85b72f2b-b78f-433d-a06e-3=
0ca7191d074?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgs=
bTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline" targe=
t=3D"_blank">Electric Slide</a><span>, wrestles with the strategic logic of=
 betting the future on AI, and ends with cautious optimism about America=E2=
=80=99s ability to rebuild and win in the Electric Era.  </span></p><p styl=
e=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"=
><span>If you want to jump straight to the online version: </span><strong><=
a href=3D"https://substack.com/redirect/c70b44e2-b0f1-4826-bef6-90a6f061e51=
d?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=
=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline" target=3D"_bl=
ank">Read The Electric Slide Online</a></strong></p><p style=3D"margin:0 0 =
20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><span>If you wa=
nt it as a PDF, you can download it here: </span><strong><a href=3D"https:/=
/substack.com/redirect/8633fa4e-b8a9-44d0-a9d7-88b43fbfd42b?j=3DeyJ1IjoiZ2d=
0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"colo=
r:rgb(54,55,55);text-decoration:underline" target=3D"_blank">Electric Slide=
 PDF</a></strong></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line=
-height:26px;font-size:16px">Let=E2=80=99s get to it. </p><div style=3D"fon=
t-size:16px;line-height:26px"><hr style=3D"margin:32px 0;padding:0;height:1=
px;background:#e6e6e6;border:none"></div><h4 style=3D"font-family:&#39;SF P=
ro Display&#39;,-apple-system-headline,system-ui,-apple-system,BlinkMacSyst=
emFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Colo=
r Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;font-weight=
:bold;margin:1em 0 0.625em 0;color:rgb(54,55,55);line-height:1.16em;font-si=
ze:1.125em"><strong><span>Today=E2=80=99s Not Boring is brought to you by=
=E2=80=A6 </span><a href=3D"https://substack.com/redirect/0d28bb35-fda0-475=
0-a61a-f4411791453f?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74Uog=
Z1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:underlin=
e" target=3D"_blank">Vanta</a></strong></h4><div style=3D"font-size:16px;li=
ne-height:26px;margin:32px auto"><table width=3D"100%" border=3D"0" cellspa=
cing=3D"0" cellpadding=3D"0"><tbody><tr><td style=3D"text-align:center"></t=
d><td align=3D"left" width=3D"1200" style=3D"text-align:center"><a href=3D"=
https://substack.com/redirect/0d28bb35-fda0-4750-a61a-f4411791453f?j=3DeyJ1=
IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=
=3D"padding:0;width:auto;height:auto;border:none;text-decoration:none;displ=
ay:block;margin:0" target=3D"_blank"><img alt=3D"" title=3D"" width=3D"550"=
 height=3D"195.70833333333334" src=3D"https://substackcdn.com/image/fetch/$=
s_!BPlK!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F=
%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79449f43-8ad3-4=
7a4-b069-eaad4de878e8_1200x427.png" style=3D"border:none!important;vertical=
-align:middle;display:block;height:auto;margin-bottom:0;width:auto!importan=
t;max-width:100%!important;margin:0 auto"></a></td><td style=3D"text-align:=
center"></td></tr></tbody></table></div><p style=3D"margin:0 0 20px 0;color=
:rgb(54,55,55);line-height:26px;font-size:16px"><em><a href=3D"https://subs=
tack.com/redirect/0d28bb35-fda0-4750-a61a-f4411791453f?j=3DeyJ1IjoiZ2d0YWYi=
fQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb=
(54,55,55);text-decoration:underline" target=3D"_blank">Vanta</a><span> hel=
ps growing companies achieve compliance quickly and painlessly by automatin=
g 35+ frameworks, including SOC 2, ISO 27001, HIPAA, and more.</span></em><=
/p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-=
size:16px"><em><span>Start with </span><a href=3D"https://substack.com/redi=
rect/0d28bb35-fda0-4750-a61a-f4411791453f?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS3=
4PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);te=
xt-decoration:underline" target=3D"_blank">Vanta=E2=80=99s Compliance for S=
tartups Bundle</a><span>, with key resources to accelerate your journey: st=
ep-by-step compliance checklists, case studies from fast-growing startups, =
and on-demand videos with industry leaders.</span></em></p><p style=3D"marg=
in:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><em><str=
ong><a href=3D"https://substack.com/redirect/0d28bb35-fda0-4750-a61a-f44117=
91453f?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" =
rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline" target=3D"=
_blank">Get it here</a><span>.</span></strong></em></p><div style=3D"font-s=
ize:16px;line-height:26px"><hr style=3D"margin:32px 0;padding:0;height:1px;=
background:#e6e6e6;border:none"></div><h1 style=3D"font-family:&#39;SF Pro =
Display&#39;,-apple-system-headline,system-ui,-apple-system,BlinkMacSystemF=
ont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Color E=
moji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;font-weight:bo=
ld;margin:1em 0 0.625em 0;color:rgb(54,55,55);line-height:1.16em;font-size:=
2em">The Electric Slide</h1><div style=3D"font-size:16px;line-height:26px;m=
argin:32px auto"><table width=3D"100%" border=3D"0" cellspacing=3D"0" cellp=
adding=3D"0"><tbody><tr><td style=3D"text-align:center"></td><td align=3D"l=
eft" width=3D"1200" style=3D"text-align:center"><a href=3D"https://substack=
.com/redirect/04120d4c-243e-4b7c-93da-4ccfe804a348?j=3DeyJ1IjoiZ2d0YWYifQ.A=
RMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"padding:0;wid=
th:auto;height:auto;border:none;text-decoration:none;display:block;margin:0=
" target=3D"_blank"><img alt=3D"" title=3D"" width=3D"550" height=3D"275" s=
rc=3D"https://substackcdn.com/image/fetch/$s_!dx_M!,w_1100,c_limit,f_auto,q=
_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazon=
aws.com%2Fpublic%2Fimages%2F596c9911-5b50-4b9e-ae47-85af022994e7_1200x600.p=
ng" style=3D"border:none!important;vertical-align:middle;display:block;heig=
ht:auto;margin-bottom:0;width:auto!important;max-width:100%!important;margi=
n:0 auto"></a></td><td style=3D"text-align:center"></td></tr></tbody></tabl=
e></div><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;=
font-size:16px"><span>One of the more interesting developments in AI is tha=
t while the American AI companies are mainly focused on closed-weight model=
s, </span><a href=3D"https://substack.com/redirect/36fda68e-d995-42f2-adf4-=
d88d63a543fc?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcg=
sbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline" targ=
et=3D"_blank">China is building open-weight models</a><span>.</span></p><p =
style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:1=
6px">That begs the question: why?</p><p style=3D"margin:0 0 20px 0;color:rg=
b(54,55,55);line-height:26px;font-size:16px">On its face, the bet is simple=
: if China doesn=E2=80=99t have access to leading-edge chips, then open-wei=
ghts are the best way to encourage both adoption and ecosystem development.=
</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font=
-size:16px">I think they=E2=80=99re making a different bet.</p><p style=3D"=
margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><spa=
n>A couple of years ago, </span><a href=3D"https://substack.com/redirect/2c=
fcd8ac-374a-4c48-9835-58901df82243?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY=
74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-deco=
ration:underline" target=3D"_blank">Isaiah Taylor</a><span>, the founder of=
 nuclear company </span><a href=3D"https://substack.com/redirect/b1cff841-c=
acd-455e-945e-7e98f7494986?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3r=
dJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:u=
nderline" target=3D"_blank">Valar Atomics</a><span>, </span><a href=3D"http=
s://substack.com/redirect/ff3d9c7c-f10e-49b9-9503-2c1702d0e0c1?j=3DeyJ1Ijoi=
Z2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"c=
olor:rgb(54,55,55);text-decoration:underline" target=3D"_blank">told me</a>=
<span> something that=E2=80=99s stuck in my head ever since:</span></p><blo=
ckquote style=3D"border-left:4px solid #0c2427;margin:20px 0;padding:0"><p =
style=3D"margin:0 0 20px 0;color:rgb(54,55,55);margin-left:20px;line-height=
:26px;font-size:16px"><em><span>There are only really three pillars to anyt=
hing around us, as far as consumable goods. We&#39;ve got </span><strong>en=
ergy, intelligence, and dexterity</strong><span>.</span></em></p></blockquo=
te><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-=
size:16px">I would generalize =E2=80=9Cdexterity=E2=80=9D to =E2=80=9Cactio=
n.=E2=80=9D Everything we see around us, and will see around us in the futu=
re, is the result of the potential to do work (energy), the capacity to dec=
ide what to do and how (intelligence), and the ability to manipulate matter=
 (action).</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height=
:26px;font-size:16px"><span>In economic terms, energy, intelligence, and ac=
tion are strong </span><strong>complements</strong><span> in the production=
 of anything.</span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);l=
ine-height:26px;font-size:16px"><span>And in the </span><a href=3D"https://=
substack.com/redirect/fe6a2ca1-f3bb-475f-b0b8-94ee3ccc2e9f?j=3DeyJ1IjoiZ2d0=
YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color=
:rgb(54,55,55);text-decoration:underline" target=3D"_blank">immortal words<=
/a><span> of Joel Spolsky, </span><strong>&quot;Smart companies try to comm=
oditize their products=E2=80=99 complements.=E2=80=9D</strong></p><p style=
=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">=
America is, implicitly or explicitly, making a bet that whoever wins intell=
igence, in the form of AI, wins the future.</p><p style=3D"margin:0 0 20px =
0;color:rgb(54,55,55);line-height:26px;font-size:16px"><strong>China is mak=
ing a different bet: that for intelligence to truly matter, it needs energy=
 and action.</strong></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);=
line-height:26px;font-size:16px">If you control energy and action, making i=
ntelligence abundant strengthens your position.</p><p style=3D"margin:0 0 2=
0px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">After catching u=
p to America in electricity generation in just 2010, China now generates 2.=
5x as much electricity as we do.</p><div style=3D"font-size:16px;line-heigh=
t:26px;margin:32px auto"><table width=3D"100%" border=3D"0" cellspacing=3D"=
0" cellpadding=3D"0"><tbody><tr><td style=3D"text-align:center"></td><td al=
ign=3D"left" width=3D"1019" style=3D"text-align:center"><a href=3D"https://=
substack.com/redirect/3f18314e-2e2a-439e-9b2b-9821ccbcb15a?j=3DeyJ1IjoiZ2d0=
YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"paddi=
ng:0;width:auto;height:auto;border:none;text-decoration:none;display:block;=
margin:0" target=3D"_blank"><img alt=3D"" title=3D"" width=3D"550" height=
=3D"326.00588812561335" src=3D"https://substackcdn.com/image/fetch/$s_!mHtl=
!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubs=
tack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4edec358-28f3-4d58-b0f=
f-59bd64801ae3_1019x604.png" style=3D"border:none!important;vertical-align:=
middle;display:block;height:auto;margin-bottom:0;width:auto!important;max-w=
idth:100%!important;margin:0 auto"></a></td><td style=3D"text-align:center"=
></td></tr></tbody></table></div><p style=3D"margin:0 0 20px 0;color:rgb(54=
,55,55);line-height:26px;font-size:16px"><span>It also dominates the techno=
logies that turn electricity into action: </span><strong>the Electric Stack=
</strong><span>.</span></p><ul style=3D"margin-top:0;padding:0"><li style=
=3D"margin:8px 0 0 32px"><p style=3D"color:rgb(54,55,55);line-height:26px;m=
argin-bottom:0;box-sizing:border-box;padding-left:4px;font-size:16px;margin=
:0"><strong>Lithium-Ion Batteries</strong></p></li><li style=3D"margin:8px =
0 0 32px"><p style=3D"color:rgb(54,55,55);line-height:26px;margin-bottom:0;=
box-sizing:border-box;padding-left:4px;font-size:16px;margin:0"><strong>Mag=
nets and Electric Motors</strong></p></li><li style=3D"margin:8px 0 0 32px"=
><p style=3D"color:rgb(54,55,55);line-height:26px;margin-bottom:0;box-sizin=
g:border-box;padding-left:4px;font-size:16px;margin:0"><strong>Power Electr=
onics</strong></p></li><li style=3D"margin:8px 0 0 32px"><p style=3D"color:=
rgb(54,55,55);line-height:26px;margin-bottom:0;box-sizing:border-box;paddin=
g-left:4px;font-size:16px;margin:0"><strong>Embedded Compute</strong></p></=
li></ul><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;=
font-size:16px">Today, China produces 75% of lithium-ion batteries globally=
 and manufactures 90% of the neodymium magnets that make motors spin. In po=
wer electronics and embedded compute, it=E2=80=99s rapidly gaining ground.<=
/p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-=
size:16px">That means that China controls the means of producing electric v=
ehicles (EVs), drones, robots, and all of the other electric products that =
are replacing the combustion-driven machines on which America built its mig=
ht.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;f=
ont-size:16px">As we speak, everything that moves, heats, lights up, comput=
es, or converts energy is being rebuilt to perform better, faster, cheaper,=
 quieter, and as a freebie, cleaner around electric technology.</p><p style=
=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">=
<strong>Simply put: anything that can go electric will.</strong></p><p styl=
e=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"=
><strong>Or rather, anything that can go electric </strong><em><strong>econ=
omically</strong></em><strong> will.</strong></p><p style=3D"margin:0 0 20p=
x 0;color:rgb(54,55,55);line-height:26px;font-size:16px">Every year, the nu=
mber of things that can economically go electric increases as their compone=
nts get cheaper and more performant. Every year, China grows its Electric S=
tack capabilities relative to the West. Taken together, that means that mor=
e of the physical cutting edge will be Made in China.</p><p style=3D"margin=
:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">And as hum=
anity infuses machines with intelligence, more of those intelligent machine=
s will be Chinese.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);lin=
e-height:26px;font-size:16px"><span>This is why China is happy commoditizin=
g AI. They believe that </span><strong>action</strong><span> is the much ha=
rder, and therefore more valuable, piece of the future to own.</span></p><p=
 style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:=
16px">To understand why China is making this bet, and why they&#39;re proba=
bly right, you need to understand what the Electric Stack is, how incredibl=
y cheap it&#39;s gotten, and who controls each layer.</p><p style=3D"margin=
:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">The deeper=
 you go, the more ridiculous it feels to believe that if we simply build th=
e best models, we will win economic and military dominance, once you apprec=
iate how all of this stuff works, how it all fits together. You need to fee=
l, in your bones, that research, great ideas, without the manufacturing mig=
ht to turn them into scaled products is no moat.</p><p style=3D"margin:0 0 =
20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">What follows is=
 a surprisingly thrilling 40,000-word story of Western invention and Easter=
n manufacturing, of GM selling our future for $70 million, of conferences i=
n Pittsburgh and assembly lines in Fukushima, of exactly how it is that dro=
nes fly, and of cost curves.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,=
55,55);line-height:26px;font-size:16px"><strong>The details matter because =
the details make the curve, and the curves are destiny.</strong></p><p styl=
e=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"=
><span>Everyone reading this is likely familiar with Moore=E2=80=99s Law. M=
any of you are likely familiar with scaling laws in AI, and Rich Sutton=E2=
=80=99s associated </span><em><a href=3D"https://substack.com/redirect/986a=
f27a-7f4e-410d-9c16-53d6b4b3996c?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74=
KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decora=
tion:underline" target=3D"_blank">Bitter Lesson</a></em><span>. Somehow, as=
 if by magic, these digital curves become self-fulfilling, their audacity a=
ttracting talent and capital that make them come true.</span></p><p style=
=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">=
These curves apply to the physical world, too.</p><p style=3D"margin:0 0 20=
px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><span>We are all =
familiar with the </span><a href=3D"https://substack.com/redirect/1a3904c3-=
76a1-4cad-8d9a-57ed8de8c03b?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3=
rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:=
underline" target=3D"_blank">solar panel cost curves</a><span>, which have =
seen solar energy drop from $130.70 per watt in 1975 to $0.31 per watt toda=
y.</span></p><div style=3D"font-size:16px;line-height:26px;margin:32px auto=
"><table width=3D"100%" border=3D"0" cellspacing=3D"0" cellpadding=3D"0"><t=
body><tr><td style=3D"text-align:center"></td><td align=3D"left" width=3D"9=
08" style=3D"text-align:center"><a href=3D"https://substack.com/redirect/ea=
da3419-f9d8-4fef-a115-8b8e65742143?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY=
74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"padding:0;width:auto;height:a=
uto;border:none;text-decoration:none;display:block;margin:0" target=3D"_bla=
nk"><img alt=3D"" title=3D"" width=3D"550" height=3D"296.2004405286344" src=
=3D"https://substackcdn.com/image/fetch/$s_!Iqf4!,w_1100,c_limit,f_auto,q_a=
uto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaw=
s.com%2Fpublic%2Fimages%2F07e91fc9-90c9-4af4-bf41-ff39abe5f08f_908x489.png"=
 style=3D"border:none!important;vertical-align:middle;display:block;height:=
auto;margin-bottom:0;width:auto!important;max-width:100%!important;margin:0=
 auto"></a></td><td style=3D"text-align:center"></td></tr></tbody></table><=
/div><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;fon=
t-size:16px"><span>This has to do with electricity </span><strong>generatio=
n</strong><span>: turning some fuel =E2=80=93 oil, coal, sunlight, wind, na=
tural gas, uranium, or water - into electrons that can be used to power pra=
ctically anything.</span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,=
55);line-height:26px;font-size:16px"><span>We are less familiar with anothe=
r set of curves: those that make up the Electric Stack. These are the LEGO =
blocks that snap together to make the products that </span><strong>consume =
</strong><span>electricity and turn it into action.</span></p><p style=3D"m=
argin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><span=
>While there is a similar curve for </span><a href=3D"https://substack.com/=
redirect/4abe205d-d0c3-49fb-aae0-e8f423a599b3?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEf=
qFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55=
);text-decoration:underline" target=3D"_blank">batteries through 2018</a><s=
pan>, there aren=E2=80=99t for the other layers of the Electric Stack, nor =
is there one Electric Stack curve. So we built them, in the hopes that they=
 attract people to build on the Electric Stack like Moore=E2=80=99s Law has=
 attracted people to build on computers.</span></p><p style=3D"margin:0 0 2=
0px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">Each curve tells=
 a story.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:=
26px;font-size:16px">Since Sony started rolling out lithium-ion batteries i=
n 1991, battery packs have gotten 98.7% cheaper, for an annual decline of 1=
2.5%.</p><div style=3D"font-size:16px;line-height:26px;margin:32px auto"><t=
able width=3D"100%" border=3D"0" cellspacing=3D"0" cellpadding=3D"0"><tbody=
><tr><td style=3D"text-align:center"></td><td align=3D"left" width=3D"1189"=
 style=3D"text-align:center"><a href=3D"https://substack.com/redirect/808d4=
7a9-3290-461b-a097-b08e8ab96a6f?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74K=
yYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"padding:0;width:auto;height:auto=
;border:none;text-decoration:none;display:block;margin:0" target=3D"_blank"=
><img alt=3D"" title=3D"" width=3D"550" height=3D"290.0336417157275" src=3D=
"https://substackcdn.com/image/fetch/$s_!_mAc!,w_1100,c_limit,f_auto,q_auto=
:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.c=
om%2Fpublic%2Fimages%2F116437f2-97cd-4217-ae26-321a974cd842_1189x627.png" s=
tyle=3D"border:none!important;vertical-align:middle;display:block;height:au=
to;margin-bottom:0;width:auto!important;max-width:100%!important;margin:0 a=
uto"></a></td><td style=3D"text-align:center"></td></tr></tbody></table><em=
>1991-2018: Ziegler &amp; Trancik MIT (adjusted to pack at 1.26x), 2019-202=
4: Bloomberg NEF</em></div><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55=
);line-height:26px;font-size:16px"><span>Since hard-disk drive motors began=
 incorporating Magnequench and Sumitomo neodymium magnets in late 1980s, th=
e cost of electromagnetic actuation has dropped 98.8% from $204/kW to $5/kW=
, for an annual decline of 12.5%:</span><span style=3D"font-size:20px">=C2=
=B9</span></p><div style=3D"font-size:16px;line-height:26px;margin:32px aut=
o"><table width=3D"100%" border=3D"0" cellspacing=3D"0" cellpadding=3D"0"><=
tbody><tr><td style=3D"text-align:center"></td><td align=3D"left" width=3D"=
1189" style=3D"text-align:center"><a href=3D"https://substack.com/redirect/=
f94ce595-a52b-4d51-a0e0-51c660d6d7f7?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdw=
ZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"padding:0;width:auto;height=
:auto;border:none;text-decoration:none;display:block;margin:0" target=3D"_b=
lank"><img alt=3D"" title=3D"" width=3D"550" height=3D"284.0201850294365" s=
rc=3D"https://substackcdn.com/image/fetch/$s_!aHBO!,w_1100,c_limit,f_auto,q=
_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazon=
aws.com%2Fpublic%2Fimages%2Fe0fc0d36-68a3-46d4-9570-1eb22d4009c8_1189x614.p=
ng" style=3D"border:none!important;vertical-align:middle;display:block;heig=
ht:auto;margin-bottom:0;width:auto!important;max-width:100%!important;margi=
n:0 auto"></a></td><td style=3D"text-align:center"></td></tr></tbody></tabl=
e><em>Source: Catalogs, teardowns, government reports, you name it.</em></d=
iv><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-=
size:16px">Since industrial companies began using variable frequency drives=
 (VFD) using B. Jayant Baliga=E2=80=99s insulated gate bipolar transistors =
(IGBT) in the late 1980s, VFD inverters have gotten 99.5% cheaper, for an a=
nnual decline of 14.5%:</p><div style=3D"font-size:16px;line-height:26px;ma=
rgin:32px auto"><table width=3D"100%" border=3D"0" cellspacing=3D"0" cellpa=
dding=3D"0"><tbody><tr><td style=3D"text-align:center"></td><td align=3D"le=
ft" width=3D"1189" style=3D"text-align:center"><a href=3D"https://substack.=
com/redirect/d026bebe-8c3c-4fb0-93e6-0c4e305658a8?j=3DeyJ1IjoiZ2d0YWYifQ.AR=
MsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"padding:0;widt=
h:auto;height:auto;border:none;text-decoration:none;display:block;margin:0"=
 target=3D"_blank"><img alt=3D"" title=3D"" width=3D"550" height=3D"282.632=
46425567706" src=3D"https://substackcdn.com/image/fetch/$s_!KCIm!,w_1100,c_=
limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-m=
edia.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7d3b664-d9f2-4e77-afa1-2d9dd9723=
62f_1189x611.png" style=3D"border:none!important;vertical-align:middle;disp=
lay:block;height:auto;margin-bottom:0;width:auto!important;max-width:100%!i=
mportant;margin:0 auto"></a></td><td style=3D"text-align:center"></td></tr>=
</tbody></table><em><a href=3D"https://substack.com/redirect/0452e039-3350-=
458a-a472-5994483b6771?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74=
UogZ1UFHcgsbTc" rel=3D"" style=3D"text-decoration:underline" target=3D"_bla=
nk">This sources and methods note needs its whole own doc (linked)</a></em>=
</div><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;fo=
nt-size:16px">And since Texas Instruments commercialized microcontrollers (=
MCUs) and digital signal processors (DSPs) in calculators and kids toys in =
the late 1970s, the cost to run a million instructions per second (DMIPS) h=
as fallen 99.9%, for an annual decline of 20% over the past 35 years:</p><d=
iv style=3D"font-size:16px;line-height:26px;margin:32px auto"><table width=
=3D"100%" border=3D"0" cellspacing=3D"0" cellpadding=3D"0"><tbody><tr><td s=
tyle=3D"text-align:center"></td><td align=3D"left" width=3D"1189" style=3D"=
text-align:center"><a href=3D"https://substack.com/redirect/97681631-62a4-4=
a3b-b621-0f0d632b6663?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74U=
ogZ1UFHcgsbTc" rel=3D"" style=3D"padding:0;width:auto;height:auto;border:no=
ne;text-decoration:none;display:block;margin:0" target=3D"_blank"><img alt=
=3D"" title=3D"" width=3D"550" height=3D"282.63246425567706" src=3D"https:/=
/substackcdn.com/image/fetch/$s_!rwQe!,w_1100,c_limit,f_auto,q_auto:good,fl=
_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpub=
lic%2Fimages%2F52ac994b-5d56-441b-b837-827013694c9f_1189x611.png" style=3D"=
border:none!important;vertical-align:middle;display:block;height:auto;margi=
n-bottom:0;width:auto!important;max-width:100%!important;margin:0 auto"></a=
></td><td style=3D"text-align:center"></td></tr></tbody></table><em><a href=
=3D"https://substack.com/redirect/30a64782-712d-468c-b7a6-db0cb125d806?j=3D=
eyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" st=
yle=3D"text-decoration:underline" target=3D"_blank">This one needs its own =
sources and methods doc, too (linked)</a></em></div><p style=3D"margin:0 0 =
20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">To the best of =
our knowledge, no one has ever built a composite of these curves: equally w=
eight each component of the Electric Stack to understand how much less it c=
osts to build an electric product today than it did in the past.</p><p styl=
e=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"=
><span>We built it, and we call it: </span><strong><a href=3D"https://subst=
ack.com/redirect/85b72f2b-b78f-433d-a06e-30ca7191d074?j=3DeyJ1IjoiZ2d0YWYif=
Q.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(=
54,55,55);text-decoration:underline" target=3D"_blank">the Electric Slide</=
a><span>.</span></strong></p><div style=3D"font-size:16px;line-height:26px;=
margin:32px auto"><table width=3D"100%" border=3D"0" cellspacing=3D"0" cell=
padding=3D"0"><tbody><tr><td style=3D"text-align:center"></td><td align=3D"=
left" width=3D"1190" style=3D"text-align:center"><a href=3D"https://substac=
k.com/redirect/ec4d3369-64e8-4b4a-a7be-f5cba0e0f9e5?j=3DeyJ1IjoiZ2d0YWYifQ.=
ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"padding:0;wi=
dth:auto;height:auto;border:none;text-decoration:none;display:block;margin:=
0" target=3D"_blank"><img alt=3D"" title=3D"" width=3D"550" height=3D"369.7=
4789915966386" src=3D"https://substackcdn.com/image/fetch/$s_!guPT!,w_1100,=
c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post=
-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad390b65-b5b0-4444-b463-1346cce=
ccb3c_1190x800.png" style=3D"border:none!important;vertical-align:middle;di=
splay:block;height:auto;margin-bottom:0;width:auto!important;max-width:100%=
!important;margin:0 auto"></a></td><td style=3D"text-align:center"></td></t=
r></tbody></table></div><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);l=
ine-height:26px;font-size:16px"><strong>It shows that the cost of the Elect=
ric Stack has fallen 99% since 1990, or 12.6% per year with an equal-weight=
ed stack.</strong></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);lin=
e-height:26px;font-size:16px"><span>No product=E2=80=99s bill of materials =
(BOM) actually has equally weighted component costs, though, and no two BOM=
s are the same. A Tesla Model 3 might spend 60% of its BOM on batteries. A =
DJI Mavic 3 drone might devote 40% of its BOM to compute. So we cooked up a=
n interactive Electric Slide that you can </span><strong><a href=3D"https:/=
/substack.com/redirect/85b72f2b-b78f-433d-a06e-30ca7191d074?j=3DeyJ1IjoiZ2d=
0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"colo=
r:rgb(54,55,55);text-decoration:underline" target=3D"_blank">play with here=
</a></strong><span>:</span></p><div style=3D"font-size:16px;line-height:26p=
x;margin:32px auto"><table width=3D"100%" border=3D"0" cellspacing=3D"0" ce=
llpadding=3D"0"><tbody><tr><td style=3D"text-align:center"></td><td align=
=3D"left" width=3D"908" style=3D"text-align:center"><a href=3D"https://subs=
tack.com/redirect/5359f163-f268-46d5-a56e-9be55af76c7a?j=3DeyJ1IjoiZ2d0YWYi=
fQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"padding:0=
;width:auto;height:auto;border:none;text-decoration:none;display:block;marg=
in:0" target=3D"_blank"><img alt=3D"" title=3D"" width=3D"550" height=3D"63=
0.5616740088105" src=3D"https://substackcdn.com/image/fetch/$s_!_GkJ!,w_110=
0,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-po=
st-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb70011ca-a749-41f7-96b7-40875=
f755027_908x1041.png" style=3D"border:none!important;vertical-align:middle;=
display:block;height:auto;margin-bottom:0;width:auto!important;max-width:10=
0%!important;margin:0 auto"></a></td><td style=3D"text-align:center"></td><=
/tr></tbody></table></div><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55)=
;line-height:26px;font-size:16px"><strong>That today China owns two layers =
of the Electric Stack almost entirely was not inevitable, or even likely</s=
trong><span>.</span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);l=
ine-height:26px;font-size:16px">The four key Electric Stack technologies we=
re invented at various points between the 1960s and 1990s in America, Japan=
, and the UK, and reached critical maturity around the same time in the 199=
0s.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;f=
ont-size:16px">Then, in many cases, we sold the future. GM sold its neo mag=
nets division, Magnequench, to China for $70 million. A123 Systems, which i=
nvented the Lithium Iron Phosphate (LFP) battery, went bankrupt and sold to=
 Wanxiang for $257 million in 2013.</p><p style=3D"margin:0 0 20px 0;color:=
rgb(54,55,55);line-height:26px;font-size:16px">Thanks to shortsighted Weste=
rn errors and farsighted Chinese industrial policy, in the commercializatio=
n phase, the Electric Stack center of gravity has moved from America and Ja=
pan to China, which dominates the stack. By controlling these four technolo=
gies, China has become the world leader in everything from EVs to drones to=
 electric bikes to robots.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55=
,55);line-height:26px;font-size:16px">A giant piece of this is that mastery=
 of this stack applies across domains, allowing market leaders like BYD to =
make everything from cars, to home energy products, to iPads, to much of th=
e world=E2=80=99s drones. Within the whole sector =E2=80=93 the components,=
 software, and expertise largely transfer =E2=80=93 meaning mastery of one =
product of the stack allows success in scaling others. Advantages compound.=
 The result has been China getting the best =E2=80=9CLEGO set=E2=80=9D in t=
he world, with regards to this stack.</p><p style=3D"margin:0 0 20px 0;colo=
r:rgb(54,55,55);line-height:26px;font-size:16px"><span>Conrad Bastable call=
s this LEGO set the </span><strong>Electric Platform. </strong><span>For a =
sobering in-depth read on this topic, read his essay, </span><em><a href=3D=
"https://substack.com/redirect/f81adfa6-5ce7-4c59-a7a2-21d027252b93?j=3DeyJ=
1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=
=3D"color:rgb(54,55,55);text-decoration:underline" target=3D"_blank">Forsak=
ing Industrialism</a></em><span>. This essay owes Conrad an enormous debt f=
or both that piece, and the conversation we had on Hyperlegible. I will ref=
erence both, explicitly or implicitly, throughout.</span></p><a href=3D"htt=
ps://substack.com/redirect/81178af3-3880-42d2-a3bc-44e0770faba0?j=3DeyJ1Ijo=
iZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" style=3D"display:b=
lock;margin:32px 0" target=3D"_blank"><img src=3D"https://substackcdn.com/i=
mage/youtube/w_728,c_limit/l_youtube_play_qyqt8q,w_120/6wc2ENUCdqA" style=
=3D"border:none!important;vertical-align:middle;max-width:100%;height:auto;=
margin:0 auto;display:block;width:100%"></a><p style=3D"margin:0 0 20px 0;c=
olor:rgb(54,55,55);line-height:26px;font-size:16px"><span>Put another way, =
over the past half-century, the technologies in the Electric Stack have got=
ten so cheap and so powerful that new entrants can build better-performing =
products than incumbents. This is true for companies - it=E2=80=99s a key e=
nabler of my </span><a href=3D"https://substack.com/redirect/3a5f62c6-ccfe-=
47bf-aefc-5215554ac966?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74=
UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:under=
line" target=3D"_blank">Vertical Integrators</a><span> thesis - and it=E2=
=80=99s also true for countries.</span></p><p style=3D"margin:0 0 20px 0;co=
lor:rgb(54,55,55);line-height:26px;font-size:16px">As the Electric Stack te=
chnologies ride down their learning curves, China can better produce more o=
f what the world wants.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55=
);line-height:26px;font-size:16px"><span>Far from just making cheap compone=
nts, its companies like BYD, DJI, and Huawei, have put themselves among the=
 world=E2=80=99s most innovative integrators. In Q4 2024, BYD passed Tesla =
in sales. Per the </span><a href=3D"https://substack.com/redirect/265015f2-=
1f0d-4265-8031-fe376351bcf0?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3=
rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:=
underline" target=3D"_blank">IEA</a><span>, =E2=80=9CChina continues to be =
the world=E2=80=99s EV manufacturing hub and is responsible for more than 7=
0% of global production.=E2=80=9D</span></p><p style=3D"margin:0 0 20px 0;c=
olor:rgb(54,55,55);line-height:26px;font-size:16px">Conversely, America is =
systematically overemphasizing the role AI will play in the future and unde=
restimating the role that electrification will play.</p><p style=3D"margin:=
0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><span>As I =
wrote in </span><em><a href=3D"https://substack.com/redirect/621eca61-8dde-=
4195-b504-ff9fa2c6c231?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74=
UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:under=
line" target=3D"_blank">Base Chapter 2</a></em><span>: =E2=80=9CWhile intel=
ligence gets all of the attention, I=E2=80=99m increasingly convinced that =
what we=E2=80=99re entering is the </span><strong>Electric Era</strong><spa=
n>. Cars, robots, flying cars, drones, appliances, boats =E2=80=93 anything=
 that can go electric is going electric, because electric performs better. =
Even intelligence is reliant on access to electricity.=E2=80=9D</span></p><=
p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size=
:16px"><strong>More broadly, America=E2=80=99s implicit stance is: we will =
specialize in high-value creative work like software, chip design, and biot=
ech research, while other countries, mainly Taiwan and China, handle the lo=
w-margin manufacturing. This is an outdated stance.</strong></p><p style=3D=
"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">Man=
ufacturing and design are inextricably linked. When you make things, you le=
arn how to make them better. You learn which parts of the underlying stack =
need to be improved, improve them, and make better products. This is a them=
e that comes up over and over again in our Electric Stack story.</p><p styl=
e=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"=
><span>Texas Instruments won the Calculator Wars because it made its own mi=
crocontrollers. Sony took lithium-ion batteries from bench-scale to mass ma=
rket scale and improved their efficiency by 50%. BYD made a lot of batterie=
s, then it started making cars, and the deep knowledge of both allowed it t=
o both bet on LFP early and develop the Blade Battery that it=E2=80=99s rid=
den to EV dominance. Not for nothing, DeepSeek was able to basically match =
OpenAI on less advanced chips because it went </span><a href=3D"https://sub=
stack.com/redirect/b901af0c-ab2d-4dfc-9be6-a8e7ea8cf4b0?j=3DeyJ1IjoiZ2d0YWY=
ifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rg=
b(54,55,55);text-decoration:underline" target=3D"_blank">deeper into the gu=
ts</a><span> of NVIDIA=E2=80=99s software than anyone else.</span></p><p st=
yle=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16p=
x"><span>Ashlee Vance, who literally </span><a href=3D"https://substack.com=
/redirect/584cc602-4078-409a-baca-859bc3b3264e?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsE=
fqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,5=
5);text-decoration:underline" target=3D"_blank">wrote the book on Elon Musk=
</a><span>, recently </span><a href=3D"https://substack.com/redirect/4af583=
17-90c0-4884-aaeb-af5608ff6557?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74Ky=
Ym3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decorati=
on:underline" target=3D"_blank">wrote that</a><span>, =E2=80=9CThe two bigg=
est U.S. manufacturing success stories of the last twenty years are Tesla a=
nd SpaceX. And this is a problem.=E2=80=9D It is not surprising that the pe=
rson who sleeps on the factory floor and claims that the factory is the pro=
duct, not to mention the entrepreneur who most heartily embraced vertical i=
ntegration, is the one running both of those companies.</span></p><p style=
=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">=
<span>As we will see, the innovations that enabled the Model 3 came from a =
deep knowledge of all of the components that make up a Tesla, and how they =
work together. This same knowledge helped Tesla thrive through the </span><=
a href=3D"https://substack.com/redirect/1783d7a0-4304-4ae1-9d6a-082417ee085=
1?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=
=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline" target=3D"_bl=
ank">COVID chip shortage</a><span>.</span></p><p style=3D"margin:0 0 20px 0=
;color:rgb(54,55,55);line-height:26px;font-size:16px"><span>Even worse, tho=
ugh, and </span><strong>if America=E2=80=99s advantage is in high-value cre=
ative work, AI capable enough to confer economic and military supremacy pac=
kages up and commoditizes that advantage.</strong></p><p style=3D"margin:0 =
0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><span>As I po=
inted out in my </span><a href=3D"https://substack.com/redirect/8baa6778-e4=
5c-4971-a2ad-d7af10b47339?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rd=
J74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:un=
derline" target=3D"_blank">conversation with Conrad</a><span>, =E2=80=9CIf =
you believe that America&#39;s advantage is the IP and the design and all o=
f that, the fact that we&#39;re racing to make that a commoditized good is =
actually super ironic in a way that I hadn&#39;t appreciated before.=E2=80=
=9D</span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height=
:26px;font-size:16px">This, again, is why China is open sourcing intelligen=
ce.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;f=
ont-size:16px">Per Clayton Christensen=E2=80=99s Law of Conservation of Att=
ractive Profits, if intelligence becomes commoditized, profits will move to=
 adjacent layers of the value chain, like the electric product in which tha=
t intelligence lives. A robot with a commoditized brain may capture more of=
 the profits in the value chain than the brains themselves, particularly if=
 open source models get good enough.</p><p style=3D"margin:0 0 20px 0;color=
:rgb(54,55,55);line-height:26px;font-size:16px"><strong>To be blunt: in the=
 Electric Era, maintaining design leadership without manufacturing leadersh=
ip is not a coherent strategic position, and one that gets less coherent th=
e better you believe AI will get.</strong></p><p style=3D"margin:0 0 20px 0=
;color:rgb(54,55,55);line-height:26px;font-size:16px">And the Electric Era =
is coming, because electric products are simply better, and because they wi=
ll keep getting better.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55=
);line-height:26px;font-size:16px">As part of my job, I get to see a little=
 bit into the future, and from what I see, electric products will win the c=
oming decades.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-he=
ight:26px;font-size:16px"><span>A few months ago, I went for a ride in </sp=
an><a href=3D"https://substack.com/redirect/2165b3a2-62b1-4db0-8a0a-d794934=
bb550?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" r=
el=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline" target=3D"_=
blank">Arc=E2=80=99s</a><span> electric boat, the ArcSport, on Lake Austin.=
 It was faster, sharper-turning, and quieter than any speedboat I=E2=80=99v=
e ever been on, and it docked itself.</span></p><p style=3D"margin:0 0 20px=
 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><span>A few weeks a=
go, I went to </span><a href=3D"https://substack.com/redirect/021d587f-0308=
-4265-b0ba-9e8839665e64?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ7=
4UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:unde=
rline" target=3D"_blank">Zipline=E2=80=99s</a><span> test site in Californi=
a and watched, with my own eyes, as the drones held perfect position thanks=
 to electric motors that can adjust thrust hundreds of times per second wit=
h perfect synchronization across multiple rotors, enabled by precise power =
electronics and real-time compute.</span></p><p style=3D"margin:0 0 20px 0;=
color:rgb(54,55,55);line-height:26px;font-size:16px"><span>MRI machines, li=
ke those used to </span><a href=3D"https://substack.com/redirect/a0035c71-e=
136-4c91-a44d-2d3cb70c4581?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3r=
dJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:u=
nderline" target=3D"_blank">detect cancer early</a><span>, depend entirely =
on powerful, precisely controlled electromagnets. Residential batteries, li=
ke </span><a href=3D"https://substack.com/redirect/2661e050-6465-4daa-8b6a-=
79b3bff768f8?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcg=
sbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline" targ=
et=3D"_blank">Base Power Company=E2=80=99s</a><span>, can=E2=80=99t back up=
 homes or balance the grid without the Electric Stack. Robots, whether mode=
rn industrial robots, surgical robots, </span><a href=3D"https://substack.c=
om/redirect/b3ad077c-a02f-4a28-b114-8f54eba11af8?j=3DeyJ1IjoiZ2d0YWYifQ.ARM=
sEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55=
,55);text-decoration:underline" target=3D"_blank">Matic=E2=80=99s</a><span>=
 floor-cleaning robot, or futuristic humanoids, are made up of servomotors,=
 sophisticated power electronics, lithium batteries, and advanced compute.<=
/span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26p=
x;font-size:16px">These products all exist today. As the cost of Electric S=
tack continues to decline and performance continues to improve, new product=
s enter the feasibility window.</p><p style=3D"margin:0 0 20px 0;color:rgb(=
54,55,55);line-height:26px;font-size:16px"><a href=3D"https://substack.com/=
redirect/b17bb39d-bf55-422a-89ba-384e4b589aa1?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEf=
qFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55=
);text-decoration:underline" target=3D"_blank">Astro Mechanica</a><span> ca=
n build efficient supersonic planes, for example, because electric motors h=
ave gotten powerful enough for their weight. Electric planes will begin to =
make sense as batteries get more dense and motors more efficient. So too wi=
ll flying cars. And if we want affordable humanoid robots, even more than s=
marter intelligence, we need better batteries, motors, inverters, and micro=
controllers.</span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);li=
ne-height:26px;font-size:16px"><strong>In fact, if we want AI to play a rol=
e in any of our physical products, they need to be rebuilt on the Electric =
Stack first, so that they can speak AI=E2=80=99s language.</strong></p><p s=
tyle=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16=
px">One of the reasons, I suspect, that America is so excited about AI and =
pays relatively little attention to electrification (which, somehow, has be=
en politicized) is that the Electric Stack is messy. It exists in the real =
world.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26p=
x;font-size:16px">It is easy to imagine that a magical digital technology w=
e don=E2=80=99t quite understand but seem to be the best at will miraculous=
ly fix what ails us. It is harder to imagine how in the world we might rebu=
ild, and improve upon, such an interconnected, physical stack of technologi=
es, a stack that has taken decades of research, luck, market forces, genius=
, and elbow grease to get to this point, and one which China so thoroughly =
dominates.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height=
:26px;font-size:16px">The time for wishful thinking is over. There is a wor=
ld to be rebuilt.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line=
-height:26px;font-size:16px">Whoever owns the Electric Stack owns the right=
 to rebuild it in their image.</p><p style=3D"margin:0 0 20px 0;color:rgb(5=
4,55,55);line-height:26px;font-size:16px">The learning curves are an incred=
ibly useful guide: they tell us where we=E2=80=99ve been, and more importan=
tly, where we=E2=80=99re going.</p><p style=3D"margin:0 0 20px 0;color:rgb(=
54,55,55);line-height:26px;font-size:16px">But the curves are too smooth fo=
r real understanding. That smoothness masks a ton of complexity: the resear=
ch, the failures, the coincidences, the business deals, the products, the i=
ndustrial planning, and the ingenuity that somehow, almost impossibly, came=
 together to create the world we live in.</p><p style=3D"margin:0 0 20px 0;=
color:rgb(54,55,55);line-height:26px;font-size:16px">So we will need to cov=
er both, and we will need to go incredibly deep, so you get a real feel for=
 the thing, for the magnitude of both the miracle and the challenge.</p><p =
style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:1=
6px">If America wants to win the future =E2=80=93 not because we=E2=80=99re=
 itching for a fight, but because we want to maintain our role as the world=
=E2=80=99s largest and most innovative economy =E2=80=93 we will need to ve=
rtically integrate. We need to have the ability to manufacture every part o=
f the Electric Stack, the understanding of how to build the best products t=
hat comes from that ability, and the ability to scale.</p><p style=3D"margi=
n:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">Getting t=
his mojo back won=E2=80=99t be easy. It seems almost impossible. It will ta=
ke industrial policy, innovation, government support, consumer demand, and =
a little free market magic to pull it off. Currently, we are shooting ourse=
lves in the steel-toed foot.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,=
55,55);line-height:26px;font-size:16px">One thing we=E2=80=99ll learn in st=
udying the history is that demand for electric products drives scale, cost =
declines, and performance improvements.</p><p style=3D"margin:0 0 20px 0;co=
lor:rgb(54,55,55);line-height:26px;font-size:16px"><span>Unfortunately, ele=
ctrification has become unnecessarily politicized in America, with cultural=
 associations obscuring the hard strategic realities. While the current adm=
inistration has shown understanding of electricity generation through nucle=
ar EOs and of component importance through investments like the Pentagon=E2=
=80=99s </span><a href=3D"https://substack.com/redirect/c19a8d3b-8862-4653-=
a6d6-96cd54a97521?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1=
UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline"=
 target=3D"_blank">$400 million in MP Materials</a><span>, the rollback of =
demand-side incentives undermines the very learning curves that could resto=
re American manufacturing dominance.</span></p><p style=3D"margin:0 0 20px =
0;color:rgb(54,55,55);line-height:26px;font-size:16px">If I were President,=
 I would make sure that every American man, woman, and child has an EV, hea=
t pump, drone, induction stove, and robot. American demand is perhaps the m=
ost powerful motor in the world, and our best shot at economically onshorin=
g enough of the Electric Stack to remain competitive in the Electric Era.</=
p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-s=
ize:16px">My hope is that by better understanding how we got here, we can a=
void mistakes like this and better determine where to go next.</p><h3 style=
=3D"font-family:&#39;SF Pro Display&#39;,-apple-system-headline,system-ui,-=
apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,s=
ans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe U=
I Symbol&#39;;font-weight:bold;margin:1em 0 0.625em 0;color:rgb(54,55,55);l=
ine-height:1.16em;font-size:1.375em"><strong>The Roadmap</strong></h3><p st=
yle=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16p=
x">This is not a short essay, nor a light one, even by Not Boring=E2=80=99s=
 standards. There are a few reasons for that.</p><p style=3D"margin:0 0 20p=
x 0;color:rgb(54,55,55);line-height:26px;font-size:16px">First and foremost=
, given what I believe to be the importance of the Electric Stack to the mo=
dern world and its future, we are woefully unfamiliar with its history and =
details.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:2=
6px;font-size:16px"><span>When I say =E2=80=9Cwe,=E2=80=9D I certainly mean=
 me. As you might be able to tell, the process of writing this essay involv=
ed a lot of =E2=80=9COH! </span><em>That=E2=80=99s</em><span> how that work=
s.=E2=80=9D Just as we hand-wave that AI will fix everything, we handwave a=
bout the components of the Electric Stack based on a headline we read in th=
e WSJ or a tweet we scrolled by in our feed.</span></p><p style=3D"margin:0=
 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">=E2=80=9CIt&=
#39;s critical that America not rely on China for batteries!=E2=80=9D Yes, =
but why, and at which level should we integrate? =E2=80=9CChina controls 90=
% of rare earth magnet production!=E2=80=9D Yes, OK, but what is a rare ear=
th magnet, what does it do, why is it important that we manufacture them he=
re, and how might we be able to do that? I hope that by diving into an insa=
ne level of historical detail, we can have more nuanced conversations about=
 the future.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-heig=
ht:26px;font-size:16px">Second, because I find this stuff fascinating. The =
tale is full of hidden legends and business case studies - triumphs and fum=
bles - that shape how the world moves.</p><p style=3D"margin:0 0 20px 0;col=
or:rgb(54,55,55);line-height:26px;font-size:16px">Any hope of getting our e=
fforts right this time requires an understanding of where they=E2=80=99ve g=
one wrong (or right) in the past.</p><p style=3D"margin:0 0 20px 0;color:rg=
b(54,55,55);line-height:26px;font-size:16px">Finally, because the curves th=
emselves tell stories, predict the future, and in so doing, bring that futu=
re into existence.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);lin=
e-height:26px;font-size:16px"><span>The components that make up modern elec=
tric products have gotten so cheap and so performant that entirely new thin=
gs are becoming possible and economical each year. And while they </span><e=
m>feel</em><span> less likely to continue because they have to interact wit=
h the physical world, somehow, they do. People keep underestimating how che=
ap solar is going to be; the same should be true for most things built on t=
he Electric Stack.</span></p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,=
55);line-height:26px;font-size:16px">That=E2=80=99s another reason to write=
 the stories in addition to simply showing the curves. Every story shows a =
technological tree that seems to have hit its last branch, before someone, =
somewhere tries a new chemistry, adds a new element, or configures the LEGO=
 blocks in just such a way that, suddenly, it just kind of works, works eno=
ugh, at least, for a specific product that really needs it to work just tha=
t way=E2=80=A6 and the rest is history. The curves continue.</p><p style=3D=
"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">The=
re=E2=80=99s a risk in an essay like this of painting one of two pictures: =
either that we must do everything in our power to beat China or that we are=
 so hopelessly behind that there=E2=80=99s no point, that we should just fo=
cus on the game we can win, even if it=E2=80=99s not the most important gam=
e.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;fo=
nt-size:16px">I think the curves tell an optimistic story: that, thanks in =
large part to Western science and Eastern manufacturing, these technologies=
 have now reached a point at which it is becoming increasingly possible to =
build an Electric world, economically.</p><p style=3D"margin:0 0 20px 0;col=
or:rgb(54,55,55);line-height:26px;font-size:16px">This is a long piece, but=
 it=E2=80=99s one that I=E2=80=99ve loved researching and writing over the =
past month, and I think it=E2=80=99s the most comprehensive resource for th=
ose who want to understand how we got here and where we might go in the Ele=
ctric Era.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height=
:26px;font-size:16px">We will cover:</p><ol style=3D"margin-top:0;padding:0=
"><li style=3D"margin:8px 0 0 32px"><p style=3D"color:rgb(54,55,55);line-he=
ight:26px;margin-bottom:0;box-sizing:border-box;padding-left:4px;font-size:=
16px;margin:0"><strong>A Brief History of Electromagnetism:</strong><span> =
The force driving the Electric Era.</span></p></li><li style=3D"margin:8px =
0 0 32px"><p style=3D"color:rgb(54,55,55);line-height:26px;margin-bottom:0;=
box-sizing:border-box;padding-left:4px;font-size:16px;margin:0"><strong>How=
 Electric Motors Work: </strong><span>Establishing the fundamentals.</span>=
</p></li><li style=3D"margin:8px 0 0 32px"><p style=3D"color:rgb(54,55,55);=
line-height:26px;margin-bottom:0;box-sizing:border-box;padding-left:4px;fon=
t-size:16px;margin:0"><strong>Lithium-Ion Batteries: </strong><span>Li-Ion,=
 NMC, NCA, Tesla, BYD, CATL, and LFP.</span></p></li><li style=3D"margin:8p=
x 0 0 32px"><p style=3D"color:rgb(54,55,55);line-height:26px;margin-bottom:=
0;box-sizing:border-box;padding-left:4px;font-size:16px;margin:0"><strong>M=
agnets and Electric Motors: </strong><span>the neodymium magnets that spin =
the world.</span></p></li><li style=3D"margin:8px 0 0 32px"><p style=3D"col=
or:rgb(54,55,55);line-height:26px;margin-bottom:0;box-sizing:border-box;pad=
ding-left:4px;font-size:16px;margin:0"><strong>The Century of Semiconductor=
s: </strong><span>the birth of compute.</span></p></li><li style=3D"margin:=
8px 0 0 32px"><p style=3D"color:rgb(54,55,55);line-height:26px;margin-botto=
m:0;box-sizing:border-box;padding-left:4px;font-size:16px;margin:0"><strong=
>Power Electronics and Control Systems:</strong><span> controlling electric=
ity with itself.</span></p></li><li style=3D"margin:8px 0 0 32px"><p style=
=3D"color:rgb(54,55,55);line-height:26px;margin-bottom:0;box-sizing:border-=
box;padding-left:4px;font-size:16px;margin:0"><strong>Embedded Compute: </s=
trong><span>microcontrollers, DSPs, ARM, and RISC-V.</span></p></li><li sty=
le=3D"margin:8px 0 0 32px"><p style=3D"color:rgb(54,55,55);line-height:26px=
;margin-bottom:0;box-sizing:border-box;padding-left:4px;font-size:16px;marg=
in:0"><strong>Lessons and Takeaways: </strong><span>What can we learn from =
the history of the Electric Stack?</span></p></li><li style=3D"margin:8px 0=
 0 32px"><p style=3D"color:rgb(54,55,55);line-height:26px;margin-bottom:0;b=
ox-sizing:border-box;padding-left:4px;font-size:16px;margin:0"><strong>Rebu=
ilding the Electric Stack: </strong><span>What it will take to build the fu=
ture.</span></p></li></ol><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55)=
;line-height:26px;font-size:16px">To be clear upfront: rebuilding the Elect=
ric Stack in the West will be hard, but possible. America still owns the gr=
eatest demand and entrepreneurial engines the world has ever seen. We will =
need to run both at about a million RPMs.</p><p style=3D"margin:0 0 20px 0;=
color:rgb(54,55,55);line-height:26px;font-size:16px">So without further ado=
, let=E2=80=99s begin. And we must begin, of course, all the way at the bot=
tom, with some fundamental physics.</p><div style=3D"font-size:16px;line-he=
ight:26px"><hr style=3D"margin:32px 0;padding:0;height:1px;background:#e6e6=
e6;border:none"></div><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);lin=
e-height:26px;font-size:16px"><span>To read the full essay online: </span><=
strong><a href=3D"https://substack.com/redirect/c70b44e2-b0f1-4826-bef6-90a=
6f061e51d?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbT=
c" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:underline" target=
=3D"_blank">Read The Electric Slide Online</a></strong></p><p style=3D"marg=
in:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px"><span>If=
 you want it as a PDF, you can download it here: </span><strong><a href=3D"=
https://substack.com/redirect/8633fa4e-b8a9-44d0-a9d7-88b43fbfd42b?j=3DeyJ1=
IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=
=3D"color:rgb(54,55,55);text-decoration:underline" target=3D"_blank">Electr=
ic Slide PDF</a></strong></p><div style=3D"font-size:16px;line-height:26px"=
><hr style=3D"margin:32px 0;padding:0;height:1px;background:#e6e6e6;border:=
none"></div><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:2=
6px;font-size:16px"><em><span>Huge thanks to Sam D=E2=80=99Amico for workin=
g on this monster with me, and to Conrad Bastable for many of the original =
ideas! Everyone </span><a href=3D"https://substack.com/redirect/4108f760-23=
61-4969-b567-16edac81f425?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rd=
J74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-decoration:un=
derline" target=3D"_blank">go buy an Impulse stove</a><span>. </span></em><=
/p><div style=3D"font-size:16px;line-height:26px"><hr style=3D"margin:32px =
0;padding:0;height:1px;background:#e6e6e6;border:none"></div><p style=3D"ma=
rgin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">That=
=E2=80=99s all for today. We=E2=80=99ll be back in your inbox on Friday wit=
h a Weekly Dose.</p><p style=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-=
height:26px;font-size:16px">Thanks for reading,</p><p style=3D"margin:0 0 2=
0px 0;color:rgb(54,55,55);line-height:26px;font-size:16px">Packy</p><div st=
yle=3D"line-height:26px;display:flex;border-top:solid 1px rgba(204,204,204,=
0.5);padding-top:1.5em;font-size:90%;margin-bottom:0"><span style=3D"displa=
y:block;margin-right:6px;min-width:24px">1</span><div style=3D"font-size:16=
px;line-height:26px;display:block"><p style=3D"margin:0 0 20px 0;color:rgb(=
54,55,55);line-height:26px;font-size:16px;min-width:10px"><span>You have no=
 idea how hard it was to find this data. It doesn=E2=80=99t exist in one pl=
ace. It=E2=80=99s everywhere, in old catalogs, YouTube teardowns, governmen=
t reports. The data isn=E2=80=99t clean: old hard-disk drives have higher $=
/kW in part because they needed so few kilowatts; the denominator was very =
high. Comparing that to a modern EV motor feels a little absurd, but it=E2=
=80=99s also how the progress actually happened, so we=E2=80=99re sticking =
with it. We used Claude and ChatGPT to help find all of the data, and you c=
an find a list of sources </span><a href=3D"https://substack.com/redirect/7=
a8af3ed-1740-4c22-abd3-efd894ca62cf?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZ=
Y74KyYm3rdJ74UogZ1UFHcgsbTc" rel=3D"" style=3D"color:rgb(54,55,55);text-dec=
oration:underline" target=3D"_blank">here</a><span>. This graph does its be=
st to normalize across and account for a bunch of different industries that=
 use electromagnetic motors, although in some cases, certain use cases achi=
eved better $/kW performance. The Tesla Model 3, for example, got below $5/=
kW. It is directionally correct, and while specific years may be off the ta=
keaway is the same: 98.8% reduction in the past 35 years.</span></p><p styl=
e=3D"margin:0 0 20px 0;color:rgb(54,55,55);line-height:26px;font-size:16px;=
min-width:10px"></p></div></div></div></div><div style=3D"margin-top:16px;f=
ont-size:16px;line-height:26px"><div style=3D"margin:32px 0 0;width:100%;bo=
x-sizing:border-box;border-top:1px solid #e6e6e6;font-size:16px;line-height=
:26px"></div><div style=3D"line-height:26px;margin:28px 0;font-family:syste=
m-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helvetica,A=
rial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;S=
egoe UI Symbol&#39;;color:#363737;font-size:16px"><table cellpadding=3D"0" =
cellspacing=3D"0" style=3D"font-family:system-ui,-apple-system,BlinkMacSyst=
emFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Colo=
r Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;color:#3637=
37;font-size:16px;width:100%"><tbody><tr><td valign=3D"middle" style=3D"wid=
th:52px"><img src=3D"https://substackcdn.com/image/fetch/$s_!EgnL!,f_auto,q=
_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazon=
aws.com%2Fpublic%2Fimages%2Ff3dfb9cd-a33c-4fb1-b21a-7bb9ce179ff5_1984x1984.=
jpeg" style=3D"box-sizing:border-box;border-radius:500000px;max-width:550px=
;border:none;vertical-align:middle;width:52px;height:52px;min-width:52px;mi=
n-height:52px;object-fit:cover;margin:0px;display:inline" width=3D"52" heig=
ht=3D"52"></td><td valign=3D"middle"><div style=3D"font-size:16px;line-heig=
ht:26px;margin-left:16px"><table cellpadding=3D"0" cellspacing=3D"0" style=
=3D"font-family:system-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#3=
9;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe=
 UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;color:#363737;font-size:16px;margi=
n-top:0;width:100%"><tbody><tr><td><div style=3D"font-size:14px;line-height=
:16px;margin-bottom:10px">A guest post by</div><a href=3D"https://substack.=
com/@derp?utm_campaign=3Dguest_post_bio&amp;utm_medium=3Demail" style=3D"co=
lor:#363737;font-weight:600;display:block;text-decoration:none;margin-botto=
m:7px" target=3D"_blank">Sam D&#39;Amico</a></td><td valign=3D"top" style=
=3D"text-align:right"><div style=3D"font-size:16px;line-height:26px;margin-=
left:50px"><a href=3D"https://substack.com/redirect/be7b02da-6563-47ba-8d7d=
-83f9318bade2?j=3DeyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHc=
gsbTc" style=3D"font-family:system-ui,-apple-system,BlinkMacSystemFont,&#39=
;Segoe UI&#39;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Color Emoji&#39=
;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;display:inline-block;b=
ox-sizing:border-box;border:none;border-radius:8px;font-size:14px;line-heig=
ht:20px;font-weight:600;text-align:center;margin:0;opacity:1;outline:none;b=
ackground-color:#0c2427;text-decoration:none!important;color:#ffffff!import=
ant;min-height:42px;height:auto;white-space:nowrap;border-width:10px 20px;p=
adding:0;border-color:#0c2427;border-style:solid" target=3D"_blank"><span s=
tyle=3D"text-decoration:none;color:#ffffff">Subscribe</span></a></div></td>=
</tr></tbody></table></div></td></tr></tbody></table></div></div><table rol=
e=3D"presentation" width=3D"100%" border=3D"0" cellspacing=3D"0" cellpaddin=
g=3D"0" style=3D"border-top:1px solid rgb(0,0,0,.1);border-bottom:1px solid=
 rgb(0,0,0,.1);min-width:100%"><tbody><tr height=3D"16"><td height=3D"16" s=
tyle=3D"font-size:0px;line-height:0">=C2=A0</td></tr><tr><td><table role=3D=
"presentation" width=3D"100%" border=3D"0" cellspacing=3D"0" cellpadding=3D=
"0" style=3D"border-bottom:1px solid rgb(0,0,0,.1)"><tbody><tr><td width=3D=
"95%"><table role=3D"presentation" width=3D"auto" border=3D"0" cellspacing=
=3D"0" cellpadding=3D"0" style=3D"width:95%;margin:0 auto"><tbody><tr><td a=
lign=3D"center"><a href=3D"https://substack.com/app-link/post?publication_i=
d=3D10025&amp;post_id=3D171945788&amp;utm_source=3Dsubstack&amp;utm_medium=
=3Demail&amp;utm_content=3Dshare&amp;utm_campaign=3Demail-share&amp;action=
=3Dshare&amp;triggerShare=3Dtrue&amp;isFreemail=3Dtrue&amp;r=3Dggtaf&amp;to=
ken=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwicG9zdF9pZCI6MTcxOTQ1Nzg4LCJpYXQiOjE3NTYyM=
TA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNzIjoicHViLTEwMDI1Iiwic3ViIjoicG9zdC1yZWFj=
dGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDHf_IJBSZJIu14HarD8" style=3D"font-family:=
system-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helvet=
ica,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&=
#39;Segoe UI Symbol&#39;;display:inline-block;font-weight:500;border:1px so=
lid rgb(0,0,0,.1);border-radius:9999px;text-transform:uppercase;font-size:1=
2px;line-height:12px;padding:9px 14px;text-decoration:none;color:rgb(119,11=
9,119);width:100%;padding-left:0;padding-right:0" target=3D"_blank"><img sr=
c=3D"https://substackcdn.com/image/fetch/$s_!rmYa!,w_36,c_scale,f_png,q_aut=
o:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare=
%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3=
D2" width=3D"18" height=3D"18" style=3D"margin-right:8px;min-width:18px;min=
-height:18px;border:none;vertical-align:middle;max-width:18px" alt=3D""><sp=
an style=3D"vertical-align:middle">Share</span></a></td></tr></tbody></tabl=
e></td></tr><tr height=3D"16"><td height=3D"16" style=3D"font-size:0px;line=
-height:0">=C2=A0</td></tr></tbody></table></td></tr><tr height=3D"16"><td =
height=3D"16" style=3D"font-size:0px;line-height:0">=C2=A0</td></tr><tr><td=
><table role=3D"presentation" width=3D"100%" border=3D"0" cellspacing=3D"0"=
 cellpadding=3D"0"><tbody><tr><td><table role=3D"presentation" width=3D"aut=
o" border=3D"0" cellspacing=3D"0" cellpadding=3D"0" style=3D"margin:0 auto"=
><tbody><tr><td style=3D"vertical-align:middle"><table role=3D"presentation=
" width=3D"auto" border=3D"0" cellspacing=3D"0" cellpadding=3D"0"><tbody><t=
r><td align=3D"center"><a href=3D"https://substack.com/app-link/post?public=
ation_id=3D10025&amp;post_id=3D171945788&amp;utm_source=3Dsubstack&amp;isFr=
eemail=3Dtrue&amp;submitLike=3Dtrue&amp;token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSw=
icG9zdF9pZCI6MTcxOTQ1Nzg4LCJyZWFjdGlvbiI6IuKdpCIsImlhdCI6MTc1NjIxMDU0OCwiZX=
hwIjoxNzU4ODAyNTQ4LCJpc3MiOiJwdWItMTAwMjUiLCJzdWIiOiJyZWFjdGlvbiJ9.hqQ2WkrF=
vp5wCoNoDb7STtUzx2XeVnb6NSneg5psw3E&amp;utm_medium=3Demail&amp;utm_campaign=
=3Demail-reaction&amp;r=3Dggtaf" style=3D"font-family:system-ui,-apple-syst=
em,BlinkMacSystemFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,sans-serif,=
&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#=
39;;display:inline-block;font-weight:500;border:1px solid rgb(0,0,0,.1);bor=
der-radius:9999px;text-transform:uppercase;font-size:12px;line-height:12px;=
padding:9px 14px;text-decoration:none;color:rgb(119,119,119)" target=3D"_bl=
ank"><img src=3D"https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale=
,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2=
FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26s=
trokeWidth%3D2" width=3D"18" height=3D"18" style=3D"margin-right:8px;min-wi=
dth:18px;min-height:18px;border:none;vertical-align:middle;max-width:18px" =
alt=3D""><span style=3D"vertical-align:middle">Like</span></a></td></tr></t=
body></table></td><td width=3D"8" style=3D"min-width:8px"></td><td style=3D=
"vertical-align:middle"><table role=3D"presentation" width=3D"auto" border=
=3D"0" cellspacing=3D"0" cellpadding=3D"0"><tbody><tr><td align=3D"center">=
<a href=3D"https://substack.com/app-link/post?publication_id=3D10025&amp;po=
st_id=3D171945788&amp;utm_source=3Dsubstack&amp;utm_medium=3Demail&amp;isFr=
eemail=3Dtrue&amp;comments=3Dtrue&amp;token=3DeyJ1c2VyX2lkIjoyNzY1ODMxMSwic=
G9zdF9pZCI6MTcxOTQ1Nzg4LCJpYXQiOjE3NTYyMTA1NDgsImV4cCI6MTc1ODgwMjU0OCwiaXNz=
IjoicHViLTEwMDI1Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.03DubsCPqADXkLOWPIFeb86bDH=
f_IJBSZJIu14HarD8&amp;r=3Dggtaf&amp;utm_campaign=3Demail-half-magic-comment=
s&amp;action=3Dpost-comment&amp;utm_source=3Dsubstack&amp;utm_medium=3Demai=
l" style=3D"font-family:system-ui,-apple-system,BlinkMacSystemFont,&#39;Seg=
oe UI&#39;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#=
39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;display:inline-block;font-=
weight:500;border:1px solid rgb(0,0,0,.1);border-radius:9999px;text-transfo=
rm:uppercase;font-size:12px;line-height:12px;padding:9px 14px;text-decorati=
on:none;color:rgb(119,119,119)" target=3D"_blank"><img src=3D"https://subst=
ackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progress=
ive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26heig=
ht%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2" width=3D"18=
" height=3D"18" style=3D"margin-right:8px;min-width:18px;min-height:18px;bo=
rder:none;vertical-align:middle;max-width:18px" alt=3D""><span style=3D"ver=
tical-align:middle">Comment</span></a></td></tr></tbody></table></td><td wi=
dth=3D"8" style=3D"min-width:8px"></td><td style=3D"vertical-align:middle">=
<table role=3D"presentation" width=3D"auto" border=3D"0" cellspacing=3D"0" =
cellpadding=3D"0"><tbody><tr><td align=3D"center"><a href=3D"https://substa=
ck.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvbm90Ym9ya=
W5nL3AvdGhlLWVsZWN0cmljLXNsaWRlP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1l=
bWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWN=
vbW1lbnQmcj1nZ3RhZiZ0b2tlbj1leUoxYzJWeVgybGtJam95TnpZMU9ETXhNU3dpY0c5emRGOX=
BaQ0k2TVRjeE9UUTFOemc0TENKcFlYUWlPakUzTlRZeU1UQTFORGdzSW1WNGNDSTZNVGMxT0Rnd=
01qVTBPQ3dpYVhOeklqb2ljSFZpTFRFd01ESTFJaXdpYzNWaUlqb2ljRzl6ZEMxeVpXRmpkR2x2=
YmlKOS4wM0R1YnNDUHFBRFhrTE9XUElGZWI4NmJESGZfSUpCU1pKSXUxNEhhckQ4IiwicCI6MTc=
xOTQ1Nzg4LCJzIjoxMDAyNSwiZiI6dHJ1ZSwidSI6Mjc2NTgzMTEsImlhdCI6MTc1NjIxMDU0OC=
wiZXhwIjoyMDcxNzg2NTQ4LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.8r=
ApQGF-8NftlJECt8_Vd3haFTpx7Yr2vFeHtSc02Oc?&amp;utm_source=3Dsubstack&amp;ut=
m_medium=3Demail" style=3D"font-family:system-ui,-apple-system,BlinkMacSyst=
emFont,&#39;Segoe UI&#39;,Roboto,Helvetica,Arial,sans-serif,&#39;Apple Colo=
r Emoji&#39;,&#39;Segoe UI Emoji&#39;,&#39;Segoe UI Symbol&#39;;display:inl=
ine-block;font-weight:500;border:1px solid rgb(0,0,0,.1);border-radius:9999=
px;text-transform:uppercase;font-size:12px;line-height:12px;padding:9px 14p=
x;text-decoration:none;color:rgb(119,119,119)" target=3D"_blank"><img src=
=3D"https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto=
:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardI=
con%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidt=
h%3D2" width=3D"18" height=3D"18" style=3D"margin-right:8px;min-width:18px;=
min-height:18px;border:none;vertical-align:middle;max-width:18px" alt=3D"">=
<span style=3D"vertical-align:middle">Restack</span></a></td></tr></tbody><=
/table></td></tr></tbody></table></td><td align=3D"right"><table role=3D"pr=
esentation" width=3D"auto" border=3D"0" cellspacing=3D"0" cellpadding=3D"0"=
><tbody><tr></tr></tbody></table></td></tr></tbody></table></td></tr><tr he=
ight=3D"16"><td height=3D"16" style=3D"font-size:0px;line-height:0">=C2=A0<=
/td></tr></tbody></table><div style=3D"color:rgb(119,119,119);text-align:ce=
nter;font-size:16px;line-height:26px;padding:24px0"><div style=3D"font-size=
:16px;line-height:26px;padding-bottom:24px"><p style=3D"list-style:none;fon=
t-family:system-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,Robo=
to,Helvetica,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI Emo=
ji&#39;,&#39;Segoe UI Symbol&#39;;padding-bottom:0;font-size:12px;line-heig=
ht:16px;margin:0;color:rgb(119,119,119);text-decoration:unset">=C2=A9 2025 =
<span>Packy McCormick</span><br>Brooklyn, NY <br><a href=3D"https://substac=
k.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90Ym9yaW5nLmNvL2FjdGlvbi9kaXNhYm=
xlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3lOelkxT0RNeE1Td2ljRzl6ZEY5cFpDSTZNV=
GN4T1RRMU56ZzRMQ0pwWVhRaU9qRTNOVFl5TVRBMU5EZ3NJbVY0Y0NJNk1UYzROemMwTmpVME9D=
d2lhWE56SWpvaWNIVmlMVEV3TURJMUlpd2ljM1ZpSWpvaVpHbHpZV0pzWlY5bGJXRnBiQ0o5Li1=
PMHFhQUJJLVg0d20xY2tzOW1SdU1qVEpnNEZ4b280eHVHSmdQQl9mZnMiLCJwIjoxNzE5NDU3OD=
gsInMiOjEwMDI1LCJmIjp0cnVlLCJ1IjoyNzY1ODMxMSwiaWF0IjoxNzU2MjEwNTQ4LCJleHAiO=
jIwNzE3ODY1NDgsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.4_kE8TeFNId=
3wpycnUcOSiVQd-26fI9-o9bAVK7PW6o?" style=3D"text-decoration:underline;color=
:rgb(119,119,119)" target=3D"_blank"><span style=3D"color:rgb(119,119,119);=
text-decoration:underline">Unsubscribe</span></a></p></div><p style=3D"padd=
ing:0 24px;font-size:12px;line-height:20px;margin:0;color:rgb(119,119,119);=
font-family:system-ui,-apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,R=
oboto,Helvetica,Arial,sans-serif,&#39;Apple Color Emoji&#39;,&#39;Segoe UI =
Emoji&#39;,&#39;Segoe UI Symbol&#39;;padding-bottom:0;margin-top:0"><a href=
=3D"https://substack.com/redirect/35c6b1d1-7dca-4979-ba6c-a8dd083ead95?j=3D=
eyJ1IjoiZ2d0YWYifQ.ARMsEfqFS34PAdwZY74KyYm3rdJ74UogZ1UFHcgsbTc" style=3D"co=
lor:rgb(119,119,119);text-decoration:none;display:inline-block;margin:0 4px=
" target=3D"_blank"><img src=3D"https://substackcdn.com/image/fetch/$s_!IzG=
P!,w_262,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubs=
tack.com%2Fimg%2Femail%2Fgeneric-app-button%402x.png" width=3D"131" alt=3D"=
Get the app" height=3D"40" style=3D"max-width:550px;border:none!important;v=
ertical-align:middle"></a><a href=3D"https://substack.com/redirect/2/eyJlIj=
oiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZ=
Gl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9v=
dGVyJmZyZWVTaWdudXBFbWFpbD1kZXN0aWZvckBnbWFpbC5jb20mcj1nZ3RhZiIsInAiOjE3MTk=
0NTc4OCwicyI6MTAwMjUsImYiOnRydWUsInUiOjI3NjU4MzExLCJpYXQiOjE3NTYyMTA1NDgsIm=
V4cCI6MjA3MTc4NjU0OCwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.sUOub=
xcRlTqQoG1WVp7ovlgNPeLa9V-4KSgY0Kn80Pc?" style=3D"color:rgb(119,119,119);te=
xt-decoration:none;display:inline-block;margin:0 4px" target=3D"_blank"><im=
g src=3D"https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto=
,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%=
2Fpublish-button%402x.png" width=3D"135" alt=3D"Start writing" height=3D"40=
" style=3D"max-width:550px;border:none!important;vertical-align:middle"></a=
></p></div></div></td><td></td></tr></tbody></table><img src=3D"https://eot=
rx.substackcdn.com/open?token=3DeyJtIjoiPDIwMjUwODI2MTIxNDAzLjMuNzQxZmNlNDl=
jYTkyNmJlNUBtZy1kMC5zdWJzdGFjay5jb20-IiwidSI6Mjc2NTgzMTEsInIiOiJkZXN0aWZvck=
BnbWFpbC5jb20iLCJkIjoibWctZDAuc3Vic3RhY2suY29tIiwicCI6MTcxOTQ1Nzg4LCJ0Ijoib=
mV3c2xldHRlciIsImEiOiJldmVyeW9uZSIsInMiOjEwMDI1LCJjIjoicG9zdCIsImYiOnRydWUs=
InBvc2l0aW9uIjoiYm90dG9tIiwiaWF0IjoxNzU2MjEwNTQ5LCJleHAiOjE3NTg4MDI1NDksIml=
zcyI6InB1Yi0wIiwic3ViIjoiZW8ifQ.GpdH4DoVJKScXP3OCGAHbevMZApDddoK2-jPAFsZ91o=
" alt=3D"" width=3D"1" height=3D"1" border=3D"0" style=3D"height:1px!import=
ant;width:1px!important;border-width:0!important;margin-top:0!important;mar=
gin-bottom:0!important;margin-right:0!important;margin-left:0!important;pad=
ding-top:0!important;padding-bottom:0!important;padding-right:0!important;p=
adding-left:0!important"><img width=3D"1" height=3D"1" alt=3D"" src=3D"http=
s://email.mg-d0.substack.com/o/eJw80EtuxCAQBNDTDLtYgI0_C85iNVB2UGwYQTORbx_N=
R9lWq0tP5Ymx53LZe64sgh172kwQsGoyo1bSGClwUjzWHQmFGGEl_r8Oi9RafFsHjw2jWgx5s3m=
aFwJ5IACuN86IaLXURs56VFoNsu_6bhrU5jEsnhY9OpjbIM_9K8iuNleZ_E_n8yliXbeCF8FyaR=
BP6EotRCQPiwfKldMnjsGqSS2Dmeb5nfB1h034rQeYUcS9udXn82wp8rUikTsQPsXNHdETx5xeR=
VJqI4oNqBy3XG6D3J-Kl6o2F_JJMdmU2eUS0y74vWGrKM9_PY1m7pUSD6v_AgAA__-3Enik"></=
div></div></div>

--000000000000bf1a7e063d592e8f--
"""

real_email_5 = """Delivered-To: yevheniia.ilchenko@destilabs.com
Received: by 2002:a05:6838:6527:b2:968:7d74:e7a4 with SMTP id ep7csp263818nkb;
        Wed, 27 Aug 2025 06:58:56 -0700 (PDT)
X-Received: by 2002:a05:6902:1884:b0:e95:32a9:908 with SMTP id 3f1490d57ef6-e9532a910b1mr15020500276.42.1756303135848;
        Wed, 27 Aug 2025 06:58:55 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1756303135; cv=none;
        d=google.com; s=arc-20240605;
        b=HXwoXUMHuGlrKfEaBPSXVc29D2bCadR7WmUgr9G5A+oPxjsoG61kRkKvAi6M0POyPK
         sLBUQvfn5mJsGNSUltg7EV3HveGxn6Yd61LC41Jb+Q8wCR8xxwtbBU7WfoNcJd/5D3tr
         pjR2j4DfoMReEPwJTimzCcjCWrLmJUTC+6/3h0irVL7vjhvzKPjNVmsspVo43A3LKFjT
         M0CkkNK3D3Ot2qzv6U1hbSei74xtlESP282EIUwh6u8aasT5tuRIMSzCmszHHWhm8hgu
         Yfbp+UcIjY8QrhULHR7b7t9YeV/EvZ9luWtkMv7k/qHA0OguNA8gNAI1uOigGCdmn7tp
         ijyg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :dkim-signature;
        bh=u67t0zNTeaw3jkA1aw8igdmI1dGpwWMdSeicRbQ/4rA=;
        fh=HAMlP18b8NkbM3RF1S047V5u0k2J0lYx0FjjO6Xqv0o=;
        b=jVIBvDtK3IxtAK87fxpdCLY5/p3bIezK6lRmQUaSo5OKu+L5ym33xcgLGF2O/skpeg
         jD7DtI4POTmMbIumMk5WNd2Y+7hyc8R55/5KKHoKrCGsFwrxR7+ys8jtcvNSOfkb/yEf
         AEzsiOiabH1rMlxWOOt7YqzQ5UW7gIPGjv2kgHdEOG8ELO7y9Ez/JAS4uBth0eyCV122
         2x6IKoYdRPSpCrijEdrk9W9CkLdmWtJZQoWRljCej1U94Ix7uznAq6ZwH3hWopD4cY59
         LzsPO1CHEsw0V/LPiOYeLbsZYASnWi3suBQIYFMlR2vwzUXnAKLdcODSvLK/P9e4li4M
         jrLg==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b="a/SyGTrU";
       spf=pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=destifor@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=neutral header.i=@destilabs.com
Return-Path: <destifor@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 3f1490d57ef6-e952c3262acsor7992632276.8.2025.08.27.06.58.55
        for <yevheniia.ilchenko@destilabs.com>
        (Google Transport Security);
        Wed, 27 Aug 2025 06:58:55 -0700 (PDT)
Received-SPF: pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b="a/SyGTrU";
       spf=pass (google.com: domain of destifor@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=destifor@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=neutral header.i=@destilabs.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20230601; t=1756303135; x=1756907935; darn=destilabs.com;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :from:to:cc:subject:date:message-id:reply-to;
        bh=u67t0zNTeaw3jkA1aw8igdmI1dGpwWMdSeicRbQ/4rA=;
        b=a/SyGTrUnBB7pUJA8D3gGac8iPy+6+yPEkbBwSqnqaJr5bmzKqlhE5ZmDTPgBlsGAK
         j5Q7FXqTAFqzPJOtbaKTlCVf2sGVwAtUIPTr1Jsy79rnlJCAMyS3zT8jzs7L88GvIFYY
         nA/TKpckds/JHrmJiIM92RbQUZHE/1UXB2K+v9i3/ccMlteaOYfSPKojoNZ8NstzjetV
         y+VmyvyGfu7UM0KAjnqjqiw69EtZkzUFqt1Hy8QTQF41kRAuZpggqnuYqRbfCIGNgUI1
         ORY6UeCMvxDyeopS13qPO8gs9fG7E23sdXsLG3eDqfcJgxLWKHmDw8S9fw/PQw7Sutzj
         iAEg==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1756303135; x=1756907935;
        h=to:subject:message-id:date:from:in-reply-to:references:mime-version
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to;
        bh=u67t0zNTeaw3jkA1aw8igdmI1dGpwWMdSeicRbQ/4rA=;
        b=mDEUtwqmnUD57f1PT4+JV5hqA75D/BVhCsgAkHhiOGymM9JRnPEs7nufxhW/WJ/bqa
         DV2DllvVQCx0dGXPp9yx2/F3YGF0wAfBudVaOnP7fhwX1Mx0CP6gUcV5017YGDSU+YMV
         kRpQEzqLpxzyMo3Qv+vXLyqrMeYCeJHpb6bcroBfaF0002KfiEkdn98MT/Nq3Jng7E57
         IBS2vBe8jxsPX7XWDTy4isZhOZjCMobTzMPiylNnP8OKVY53P4bFbfCElkf2NB5nKIS1
         JX2POqAnxXKz2X4d90dDMPUCnifTYCIl1ZOb5vWbWT1sx5PIf9EUrdiL/XscS1/YGZSw
         fmXA==
X-Gm-Message-State: AOJu0YwZnmj4UXAybJ3bDEtvLvI9chZkzWYd0o9U1TcmWRhcHAmmuAAB
	4oeNDj/4BLnWN3cpHNhO1mHK09gwbQ2JL/CSF0Gob6H4Y4JFkjmSDF0VT4Pvl3tAT0n6IFcHfCI
	DECx5/vRUrxdQasJu4nljtlJT4b7O9ISftP4PF+s=
X-Gm-Gg: ASbGncv/fVTe6N6qiXCzcRwtEutkJEEinN1F5Lv7rkxsWYJl1mN9esfNNdMuLRLWE/q
	xaJg8svm9EbHV2le5ABZ1KYYfRVdlQc7yn2lo+lJCjMdgqZGNwtXXX5svQocq4UvudSleJYAdPk
	WFHEi2qUyVLhbziQegsF5JCadeFwKjiaB+ZY3O6jklFclY047YUpQkaJP+X8SDCAPfF8rALx+4f
	krXFLFGcY2KPloQfUm0mG9s3nbwyjU+/JcxK1w0FTqhM9itR2Ovoz/g73igbOhjZHuGxdPD5TbU
	kDQDDpM=
X-Google-Smtp-Source: AGHT+IFu2IM+k5WZg+/fRN4D7cIfCe+dXyqD+DCL5m4CaQql8XkOg5o7fbJUCGw72Mva1zXt+GvjdP03VY/4tIT8kC8=
X-Received: by 2002:a05:6902:1504:b0:e95:d920:20ad with SMTP id
 3f1490d57ef6-e95d9202f8cmr10545627276.29.1756303134907; Wed, 27 Aug 2025
 06:58:54 -0700 (PDT)
MIME-Version: 1.0
References: <565964372.48450634.1756260398735@abmktmail-batch1a.marketo.org>
In-Reply-To: <565964372.48450634.1756260398735@abmktmail-batch1a.marketo.org>
From: Mykhaylo Kushnir <destifor@gmail.com>
Date: Wed, 27 Aug 2025 14:58:44 +0100
X-Gm-Features: Ac12FXwFsNfOi2Kt1JC4MwVe__DCoBFGhARwK6WcfnGl_uH8WlL43ZWw9Sh3DVw
Message-ID: <CANPfs46AZs_Ny2S2SCZtArOzhPGjxVeBBp=YP62+g8qfU6bacA@mail.gmail.com>
Subject: Fwd: [Newsletter] A force multiplier for your tech stack
To: yevheniia.ilchenko@destilabs.com
Content-Type: multipart/alternative; boundary="0000000000007961c3063d59307a"

--0000000000007961c3063d59307a
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

---------- Forwarded message ---------
From: Lucid <email@e.lucid.co>
Date: Wed, Aug 27, 2025 at 3:08=E2=80=AFAM
Subject: [Newsletter] A force multiplier for your tech stack
To: <destifor@gmail.com>


Connect teams and workflows with 100+ Lucid integrations
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=
=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=
=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=
=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=
=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=
=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C
=E2=80=8C =E2=80=8C =E2=80=8C =E2=80=8C

[image: Newsletter]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh8nHNOkL5No2g71Nki7g7_fOUAO=
udHkgqXaVbIJKeDN2N7OjOY_0t9lJZQZ3SVtuYPU=3D>
[image: Lucid]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-4RYg9CuMxPklsdefytSA0ntcN=
vB9Zs70Kep0oR49VcX2eMXINh6tCxBjYBcPFScHM=3D>
*August 2025* newsletter
Collaboration for your apps, too
More tools can make work more complicated. See how Lucid integrates with
the tools you already use to simplify and supercharge your workflows.

Featured content
[image: Featured blog post]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-miDolHjosL9Y2nY4_UnKXssJtSsc=
novV0G25COvotbdcTbnORlwmcp3NB8BAXTmX4Q5M=3D>
Lucid integrations guide
Learn how Lucid can act as a force multiplier for your tech stack, and get
tips for integrations to try based on your use case.
Get the guide
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-miDolHjosL9Y2nY4_UnKXssJtSsc=
novV0G25COvotbdcTbnORlwmcp3NB8BAXTmX4Q5M=3D>

Templates
[image: Process flowchart template with Loom]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-9TnD5IVQLh5vxpuscj2_BegAq=
W0ZK0vD49ly1ICK8LEP3BhJSHu6zaU5WlPF3GXPg=3D>
Process flowchart template with Loom
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-9TnD5IVQLh5vxpuscj2_BegAq=
W0ZK0vD49ly1ICK8LEP3BhJSHu6zaU5WlPF3GXPg=3D>
[image: Smart Jira dashboard]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhxZWCooWksXvMyAScDJtyYqyzRA=
YCePtqXmzTeRaTMVH5rwzhRFr2oS-piHijWuT7Og=3D>
Smart Jira dashboard
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhxZWCooWksXvMyAScDJtyYqyzRA=
YCePtqXmzTeRaTMVH5rwzhRFr2oS-piHijWuT7Og=3D>
[image: Getting started with airfocus]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh6o4f6hDN7vGiSxt9RxNOeR01wF=
X_BjUKLbd_JEjn8KTs7our2uzAnJ7WrrsyHSWXDM=3D>
Getting started with airfocus
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh6o4f6hDN7vGiSxt9RxNOeR01wF=
X_BjUKLbd_JEjn8KTs7our2uzAnJ7WrrsyHSWXDM=3D>
[image: =E2=80=9CThis or that?=E2=80=9D icebreaker in collaboration with Zo=
om]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh16w3UJ_LZDARmosQD06DV-zc83=
I7sg3egrw-6dulhO-fBEVFo7jJI9WLk6dR11IA04=3D>
=E2=80=9CThis or that?=E2=80=9D icebreaker in collaboration with Zoom
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh16w3UJ_LZDARmosQD06DV-zc83=
I7sg3egrw-6dulhO-fBEVFo7jJI9WLk6dR11IA04=3D>

New capabilities
[image: New features]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_vMTbJiYWkJO7qKR2o-77qbc1K=
rNngBuhp5jNzKS297jcWH-p3EAzrBfDUqTlQf35w=3D>
Process Accelerator
With the Process Accelerator (now available!), you can standardize how
processes are documented, published, and stored across your organization.
=E2=9E=94 See how
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_vMTbJiYWkJO7qKR2o-77qbc1K=
rNngBuhp5jNzKS297jcWH-p3EAzrBfDUqTlQf35w=3D>
Google Chat integration
Help teams stay aligned by bringing visual context into conversations. When
you share a Lucid link in Google Chat, a preview of your document instantly
appears.
=E2=9E=94 Learn more
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_oDA3dOm7JWM_wv5l3ZCPmJ8uX=
ZbECpy6cWwMfjtsHwK7O2Sj4AY9mpw1Kn1GIf6AA=3D>
BPMN import
Import BPMN files from any other tool into Lucid. Don=E2=80=99t lose your w=
ork or
your momentum.
=E2=9E=94 Get the details
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh9RxFU4JHtdppQFCISOnH7PtL8m=
8pEGprZWH_m-N-KoJeslu-ehE-HW9v2rwNqbeoGc=3D>

Integrations spotlight
[image: Integrations]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhyhNz9Cg2lWF14DQJWGKIcFbF3w=
eVXGPhJJyl9Hq5_1UHV0K1Gqs-Thq3K47e8LC1pM=3D>
Google Workspace
Learn how Lucid integrates with Google Workspace, and see an example of
what using Lucid and Google together could look like.
=E2=9E=94 Dive deeper
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhyhNz9Cg2lWF14DQJWGKIcFbF3w=
eVXGPhJJyl9Hq5_1UHV0K1Gqs-Thq3K47e8LC1pM=3D>
Lucid Cards for Jira
Watch this video about leveraging Lucid Cards for Jira to visualize planned
work, manage tasks, and improve team workflows.
=E2=9E=94 Watch now
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhwETzmrKEi67nczcPRbc98jW0Au=
bZuZZSS-S9j55lhLbkbIfhBnHAcmwP7WdbwPW0S4=3D>

Lucid + airfocus
[image: New features]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_E3Z8hXhcSKp6K-k-4aiZg4lVZ=
qkoeKCa3gpOVUqKhBY1KyW26E93bsLgbUJtg9pGg=3D>
Connected product management
Together, Lucid and airfocus provide a seamless transition from
unstructured to structured work. See how product teams benefit from
integrating the two platforms.
=E2=9E=94 Learn more
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_E3Z8hXhcSKp6K-k-4aiZg4lVZ=
qkoeKCa3gpOVUqKhBY1KyW26E93bsLgbUJtg9pGg=3D>

Expert tips
[image: Expert tip]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-miB5QY84heCTJE0X22i9Yw6YV5Xt=
6SIDSBEavRh7e8WYLoHrMSdZy85A1_ku9RiWNtWU=3D>
Prioritization in IT
David Torgerson, Lucid=E2=80=99s VP of infrastructure and IT, recently shar=
ed tips
for prioritizing requests and tasks: =E2=80=9CYou can=E2=80=99t make a good=
 decision
without good data=E2=80=94that=E2=80=99s called guessing.=E2=80=9D He recom=
mends using Lucid
integrations to make informed decisions.
Learn more from Torgy
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-miB5QY84heCTJE0X22i9Yw6YV5Xt=
6SIDSBEavRh7e8WYLoHrMSdZy85A1_ku9RiWNtWU=3D>
Most connected
When customers integrate Lucid into their technology ecosystem, they
increase everything from collaboration and efficiency to data access and
cost savings. Contact us to learn about additional integrations available
with a Lucid Enterprise plan.
Talk with sales
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh1k74SuByYEDdr-WhEommbRig_D=
yWlQ0QyYvbtll_aJAugaltmK1lILlDpzYVJIPwS8=3D>
[image: Lucid] [image: Lucid]
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-4RYg9CuMxPklsdefytSA0ntcN=
vB9Zs70Kep0oR49VcX2eMXINh6tCxBjYBcPFScHM=3D>
Unsubscribe
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh8kYv2izx21Pi8CHlnqUYbKIjV8=
7KD3AviujzB_b2sSaY1sqOkEviHvFE1RsNFoTubE=3D>

Lucid Software Inc.
10355 South Jordan Gateway, Suite 300
South Jordan, UT 84095 USA
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh8nHNOkL5No2g71Nki7g7_fOUAO=
udHkgqXaVbIJKeDN2N7OjOY_0t9lJZQZ3SVtuYPU=3D>

By continuing to use Lucid's products, you agree to our Terms of Service
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-IhXfyW3A21GJGYfVRqXYnABib=
47OXMp7qMGakm_8e5hmfARJp9d_Vcjn2ARIN5IBU=3D>
and acknowledge our Privacy Policy
<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh3157ebIaPCB6yceTwOPKj04w3i=
8HrHXKgL5IZBHVPBVk6qlJRlNzKk7-16GBoIAICc=3D>.

<https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh0FYk1N5ar0GSqvSRuSmNHk-dCR=
TX0BdH6vNwpWFqimRW0ZcPeqpPMUxQ0EZdN20zFA=3D>

--0000000000007961c3063d59307a
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr"><br><br><div class=3D"gmail_quote gmail_quote_container"><=
div dir=3D"ltr" class=3D"gmail_attr">---------- Forwarded message ---------=
<br>From: <strong class=3D"gmail_sendername" dir=3D"auto">Lucid</strong> <s=
pan dir=3D"auto">&lt;<a href=3D"mailto:email@e.lucid.co">email@e.lucid.co</=
a>&gt;</span><br>Date: Wed, Aug 27, 2025 at 3:08=E2=80=AFAM<br>Subject: [Ne=
wsletter] A force multiplier for your tech stack<br>To:  &lt;<a href=3D"mai=
lto:destifor@gmail.com">destifor@gmail.com</a>&gt;<br></div><br><br><div cl=
ass=3D"msg-6107646127073961995"><u></u>

=20
=20
=20
=20
=20
=20
=20
=20
=20
=20
=20
=20
=20
=20
<div width=3D"100%" style=3D"Margin:0;background-color:#fafbfc;margin:0 aut=
o;padding:0;height:100%;width:100%">=20
<div style=3D"display:none;font-size:1px;color:#333333;line-height:1px;max-=
height:0px;max-width:0px;opacity:0;overflow:hidden">
 Connect teams and workflows with 100+ Lucid integrations =E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=
=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=20
</div>=20
<div lang=3D"en">=20
<table cellpadding=3D"0" cellspacing=3D"0" border=3D"0" width=3D"100%" heig=
ht=3D"100%" bgcolor=3D"#FAFBFC">=20
<tbody>=20
<tr>=20
<td valign=3D"top" style=3D"font-family:Arial,Helvetica,Verdana,sans-serif;=
font-size:20px;line-height:28px;color:#282c33">=20
<center style=3D"width:100%">=20
<div style=3D"max-width:680px">=20
=20
<div style=3D"line-height:0;background-color:#282c33">=20
<a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh8nHNOkL5No2g71Nk=
i7g7_fOUAOudHkgqXaVbIJKeDN2N7OjOY_0t9lJZQZ3SVtuYPU=3D" target=3D"_blank"> <=
img src=3D"https://cdn-cashy-static-assets.lucidchart.com/marketing/emails/=
Newsletters/Newsletter_header_line.png" alt=3D"Newsletter" border=3D"0" wid=
th=3D"680" style=3D"width:100%;max-width:680px;text-align:bottom;padding-bo=
ttom:0px;background-color:#282c33"></a>
</div>
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%" alig=
n=3D"center" style=3D"max-width:680px;background-color:#ffffff">=20
<tbody>=20
<tr> =20
</tr>=20
<tr>=20
<td style=3D"background-color:#282c33">=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%">=20
<tbody>
<tr>=20
<td align=3D"center" valign=3D"middle" style=3D"padding:0px" width=3D"180">=
=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%">=20
<tbody>
<tr>
 <td align=3D"left" valign=3D"middle" width=3D"80" height=3D"100%" style=3D=
"font-size:0;padding:35px 24px 0px 60px" class=3D"m_-6107646127073961995log=
o">
<a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-4RYg9CuMxPklsde=
fytSA0ntcNvB9Zs70Kep0oR49VcX2eMXINh6tCxBjYBcPFScHM=3D" target=3D"_blank"><i=
mg src=3D"https://cdn-cashy-static-assets.lucidchart.com/marketing/emails/M=
arketo-Images/Lucid-Primary-Logo-White-onClear-np-RGB@2x.png" width=3D"80" =
alt=3D"Lucid" style=3D"border:0;width:80px;max-width:80px;vertical-align:mi=
ddle" class=3D"m_-6107646127073961995logo-img">
</a>
</td>=20
</tr>=20
</tbody>
</table> </td>=20
<td style=3D"padding:0px 20px 0px 0px;color:#ffffff;width:60%" class=3D"m_-=
6107646127073961995newsletter-subheader" width=3D"60%">=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%">=20
<tbody>
<tr>=20
<td align=3D"right" valign=3D"bottom" style=3D"padding:40px 20px 0px 0px;fo=
nt-size:20px;line-height:28px;max-width:224px;color:#ffffff" class=3D"m_-61=
07646127073961995newsletter-subheader"> <b>August=C2=A02025</b> newsletter =
</td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr style=3D"background-color:#282c33">=20
<td style=3D"padding:40px 60px 20px 60px;font-size:58px;line-height:60px;fo=
nt-weight:bold;text-align:left;color:#ffffff" class=3D"m_-61076461270739619=
95header" align=3D"left">Collaboration for your apps, too</td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 40px 60px;background-color:#2=
82c33;font-size:20px;line-height:28px;color:#ffffff" class=3D"m_-6107646127=
073961995intro-text">More tools can make work more complicated. See how Luc=
id integrates with the tools you already use to simplify and supercharge yo=
ur workflows. </td>=20
</tr>=20
<tr>=20
<td align=3D"left" style=3D"padding:40px 60px 20px 60px;background-color:#c=
fe4ff;vertical-align:top;max-width:100%" class=3D"m_-6107646127073961995sec=
tion-label-pad" valign=3D"top">=20
<div style=3D"padding:1px 10px;background:#edf5ff;border:1px solid #edf5ff;=
text-decoration:none;color:#1071e5;border-radius:4px;font-size:16px;font-we=
ight:700">=20
=20
<span>Featured content</span>=20
=20
</div> </td>=20
</tr>=20
<tr>=20
<td align=3D"center" valign=3D"middle" style=3D"padding:0px 60px 10px 60px;=
background-color:#cfe4ff" class=3D"m_-6107646127073961995img"> <a href=3D"h=
ttps://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-miDolHjosL9Y2nY4_UnKXssJtSscno=
vV0G25COvotbdcTbnORlwmcp3NB8BAXTmX4Q5M=3D" target=3D"_blank"><img class=3D"=
m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets.lucid=
chart.com/marketing/emails/Newsletters/25-August/header.png" width=3D"560" =
alt=3D"Featured blog post" style=3D"border:0;width:100%;max-width:560px;ver=
tical-align:middle"></a> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px;background-color:#cfe4ff;text=
-align:left;font-size:20px;line-height:28px;font-weight:bold" class=3D"m_-6=
107646127073961995subheader1" align=3D"left">Lucid integrations guide </td>=
=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:0px 60px 10px 60px;font-size:18px;line-=
height:28px;background-color:#cfe4ff" class=3D"m_-6107646127073961995text1"=
>Learn how Lucid can act as a force multiplier for your tech stack, and get=
 tips for integrations to try based on your use case. </td>=20
</tr>=20
<tr>=20
<td align=3D"left" style=3D"padding:10px 60px 40px 60px;font-size:20px;line=
-height:28px;vertical-align:top;background-color:#cfe4ff" class=3D"m_-61076=
46127073961995button-pad2" valign=3D"top">=20
 <a align=3D"center" href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-=
miDolHjosL9Y2nY4_UnKXssJtSscnovV0G25COvotbdcTbnORlwmcp3NB8BAXTmX4Q5M=3D" st=
yle=3D"font-family:Arial,Helvetica,Verdana,sans-serif;font-size:20px;backgr=
ound-color:#282c33;text-decoration:none;padding:.5em 2em;color:#ffffff;disp=
lay:inline-block;border-radius:4px;font-weight:bold" class=3D"m_-6107646127=
073961995button2" target=3D"_blank"><span>Get the guide</span> </a>=20
 </td>=20
</tr>=20
<tr>=20
<td align=3D"left" style=3D"padding:40px 60px 10px 60px;background-color:#2=
82c33;vertical-align:top;max-width:100%" class=3D"m_-6107646127073961995sec=
tion-label-pad" valign=3D"top">=20
<div style=3D"padding:1px 10px;background:#edf5ff;border:1px solid #edf5ff;=
text-decoration:none;color:#1071e5;border-radius:4px;font-size:16px;font-we=
ight:700">=20
=20
<span>Templates</span>=20
=20
</div> </td>=20
</tr>=20
<tr>=20
<td>=20
<table cellspacing=3D"0" width=3D"100%" role=3D"presentation" style=3D"capt=
ion-side:top;width:100%">=20
<tbody>
<tr>=20
<td class=3D"m_-6107646127073961995templates" width=3D"219" align=3D"center=
" valign=3D"top" style=3D"padding:30px 19px 20px 60px;width:100%;max-width:=
100%;background-color:#282c33">=20
<table cellspacing=3D"0" width=3D"100%" role=3D"presentation" style=3D"capt=
ion-side:top;width:100%">=20
<tbody>
<tr>=20
<td width=3D"219" align=3D"center" valign=3D"top" style=3D"padding:20px 20p=
x 0px 20px;background-color:#ffffff;font-size:0px;line-height:0px;vertical-=
align:middle" class=3D"m_-6107646127073961995template-image"> <a href=3D"ht=
tps://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-9TnD5IVQLh5vxpuscj2_BegAqW0Z=
K0vD49ly1ICK8LEP3BhJSHu6zaU5WlPF3GXPg=3D" target=3D"_blank"> <img class=3D"=
m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets.lucid=
chart.com/marketing/emails/Newsletters/25-August/Process_flowchart_with_Loo=
m.png" alt=3D"Process flowchart template with Loom" border=3D"0" width=3D"2=
19"> </a> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:20px 20px 25px 20px;font-size:20px;line=
-height:28px;background-color:#ffffff" class=3D"m_-6107646127073961995templ=
ate-subheader"> <a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh=
-9TnD5IVQLh5vxpuscj2_BegAqW0ZK0vD49ly1ICK8LEP3BhJSHu6zaU5WlPF3GXPg=3D" styl=
e=3D"font-weight:bold;color:#282c33" class=3D"m_-6107646127073961995link-da=
rk" target=3D"_blank">Process flowchart template with Loom</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
<td class=3D"m_-6107646127073961995templates" width=3D"219" align=3D"center=
" valign=3D"top" style=3D"padding:30px 60px 20px 19px;width:100%;max-width:=
100%;background-color:#282c33">=20
<table cellspacing=3D"0" width=3D"100%" role=3D"presentation" style=3D"capt=
ion-side:top;width:100%">=20
<tbody>
<tr>=20
<td width=3D"219" align=3D"center" valign=3D"top" style=3D"padding:20px 20p=
x 0px 20px;background-color:#ffffff;font-size:0px;line-height:0px;vertical-=
align:middle" class=3D"m_-6107646127073961995template-image"> <a href=3D"ht=
tps://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhxZWCooWksXvMyAScDJtyYqyzRAYCe=
PtqXmzTeRaTMVH5rwzhRFr2oS-piHijWuT7Og=3D" target=3D"_blank"> <img class=3D"=
m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets.lucid=
chart.com/marketing/emails/Newsletters/25-August/Smart_Jira_dashboard.png" =
alt=3D"Smart Jira dashboard" border=3D"0" width=3D"219"> </a> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:20px 20px 53px 20px;background-color:#f=
fffff;font-size:20px;line-height:28px" class=3D"m_-6107646127073961995templ=
ate-subheader"> <a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh=
xZWCooWksXvMyAScDJtyYqyzRAYCePtqXmzTeRaTMVH5rwzhRFr2oS-piHijWuT7Og=3D" styl=
e=3D"font-weight:bold;color:#282c33" class=3D"m_-6107646127073961995link-da=
rk" target=3D"_blank">Smart Jira dashboard</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td class=3D"m_-6107646127073961995templates" width=3D"219" align=3D"center=
" valign=3D"top" style=3D"padding:20px 19px 40px 60px;width:100%;max-width:=
100%;background-color:#282c33">=20
<table cellspacing=3D"0" width=3D"100%" role=3D"presentation" style=3D"capt=
ion-side:top;width:100%">=20
<tbody>
<tr>=20
<td width=3D"219" align=3D"center" valign=3D"top" style=3D"padding:20px 20p=
x 0px 20px;background-color:#ffffff;font-size:0px;line-height:0px;vertical-=
align:middle" class=3D"m_-6107646127073961995template-image"> <a href=3D"ht=
tps://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh6o4f6hDN7vGiSxt9RxNOeR01wFX_B=
jUKLbd_JEjn8KTs7our2uzAnJ7WrrsyHSWXDM=3D" target=3D"_blank"> <img class=3D"=
m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets.lucid=
chart.com/marketing/emails/Newsletters/25-August/Getting_started_with_airfo=
cus.png" alt=3D"Getting started with airfocus" border=3D"0" width=3D"219"> =
</a> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:20px 20px 81px 20px;background-color:#f=
fffff;font-size:20px;line-height:28px" class=3D"m_-6107646127073961995templ=
ate-subheader"> <a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh=
6o4f6hDN7vGiSxt9RxNOeR01wFX_BjUKLbd_JEjn8KTs7our2uzAnJ7WrrsyHSWXDM=3D" styl=
e=3D"font-weight:bold;color:#282c33" class=3D"m_-6107646127073961995link-da=
rk" target=3D"_blank">Getting started with airfocus</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
<td class=3D"m_-6107646127073961995templates" width=3D"219" align=3D"center=
" valign=3D"top" style=3D"padding:20px 60px 40px 19px;width:100%;max-width:=
100%;background-color:#282c33">=20
<table cellspacing=3D"0" width=3D"100%" role=3D"presentation" style=3D"capt=
ion-side:top;width:100%">=20
<tbody>
<tr>=20
<td width=3D"219" align=3D"center" valign=3D"top" style=3D"padding:20px 20p=
x 0px 20px;background-color:#ffffff;font-size:0px;line-height:0px;vertical-=
align:middle" class=3D"m_-6107646127073961995template-image"> <a href=3D"ht=
tps://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh16w3UJ_LZDARmosQD06DV-zc83I7s=
g3egrw-6dulhO-fBEVFo7jJI9WLk6dR11IA04=3D" target=3D"_blank"> <img class=3D"=
m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets.lucid=
chart.com/marketing/emails/Newsletters/25-August/Zoom_icebreaker.png" alt=
=3D"=E2=80=9CThis or that?=E2=80=9D icebreaker in collaboration with Zoom" =
border=3D"0" width=3D"219"> </a> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:20px 20px 25px 20px;background-color:#f=
fffff;font-size:20px;line-height:28px" class=3D"m_-6107646127073961995templ=
ate-subheader"> <a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh=
16w3UJ_LZDARmosQD06DV-zc83I7sg3egrw-6dulhO-fBEVFo7jJI9WLk6dR11IA04=3D" styl=
e=3D"font-weight:bold;color:#282c33" class=3D"m_-6107646127073961995link-da=
rk" target=3D"_blank">=E2=80=9CThis or that?=E2=80=9D icebreaker in collabo=
ration with Zoom</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td align=3D"left" style=3D"padding:40px 60px 20px 60px;background-color:#c=
fe4ff;vertical-align:top;max-width:100%" class=3D"m_-6107646127073961995sec=
tion-label-pad" valign=3D"top">=20
<div style=3D"padding:1px 10px;background:#edf5ff;border:1px solid #edf5ff;=
text-decoration:none;color:#1071e5;border-radius:4px;font-size:16px;font-we=
ight:700">=20
=20
<span>New capabilities</span>=20
=20
</div> </td>=20
</tr>=20
<tr>=20
<td align=3D"center" valign=3D"middle" style=3D"padding:0px 60px 10px 60px;=
background-color:#cfe4ff" class=3D"m_-6107646127073961995img"> <a href=3D"h=
ttps://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_vMTbJiYWkJO7qKR2o-77qbc1KrN=
ngBuhp5jNzKS297jcWH-p3EAzrBfDUqTlQf35w=3D" target=3D"_blank"><img class=3D"=
m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets.lucid=
chart.com/marketing/emails/Newsletters/25-August/New_feature.png" width=3D"=
460" alt=3D"New features" style=3D"border:0;width:100%;max-width:460px;vert=
ical-align:middle"></a> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 0px 60px;font-size:20px;line-=
height:28px;background-color:#cfe4ff;text-align:left;font-weight:bold" clas=
s=3D"m_-6107646127073961995subheader1" align=3D"left">Process Accelerator <=
/td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 10px 60px;background-color:#c=
fe4ff;font-size:18px" class=3D"m_-6107646127073961995text1">With the Proces=
s Accelerator (now available!), you can standardize how processes are docum=
ented, published, and stored across your organization. </td>=20
</tr>=20
<tr>=20
<td>=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%" bgco=
lor=3D"#CFE4FF">=20
<tbody>
<tr>=20
<td width=3D"50" align=3D"center" style=3D"padding:12px 0px 20px 60px" clas=
s=3D"m_-6107646127073961995icon"> <span class=3D"m_-6107646127073961995arw"=
>=E2=9E=94</span> </td>=20
<td style=3D"padding:10px 40px 20px 15px;width:100%;max-width:224px;font-si=
ze:18px;text-align:left" class=3D"m_-6107646127073961995text-CTA"> <a href=
=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_vMTbJiYWkJO7qKR2o-77qb=
c1KrNngBuhp5jNzKS297jcWH-p3EAzrBfDUqTlQf35w=3D" style=3D"color:#282c33;text=
-align:left" class=3D"m_-6107646127073961995link" target=3D"_blank">See how=
</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 0px 60px;font-size:20px;line-=
height:28px;background-color:#cfe4ff;text-align:left;font-weight:bold" clas=
s=3D"m_-6107646127073961995subheader1" align=3D"left">Google Chat integrati=
on </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 10px 60px;background-color:#c=
fe4ff;font-size:18px" class=3D"m_-6107646127073961995text1">Help teams stay=
 aligned by bringing visual context into conversations. When you share a Lu=
cid link in Google Chat, a preview of your document instantly appears. </td=
>=20
</tr>=20
<tr>=20
<td>=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%" bgco=
lor=3D"#CFE4FF">=20
<tbody>
<tr>=20
<td width=3D"50" align=3D"center" style=3D"padding:12px 0px 20px 60px" clas=
s=3D"m_-6107646127073961995icon"> <span class=3D"m_-6107646127073961995arw"=
>=E2=9E=94</span> </td>=20
<td style=3D"padding:10px 40px 20px 15px;width:100%;max-width:224px;font-si=
ze:18px;text-align:left" class=3D"m_-6107646127073961995text-CTA"> <a href=
=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_oDA3dOm7JWM_wv5l3ZCPmJ=
8uXZbECpy6cWwMfjtsHwK7O2Sj4AY9mpw1Kn1GIf6AA=3D" style=3D"color:#282c33;text=
-align:left" class=3D"m_-6107646127073961995link" target=3D"_blank">Learn m=
ore</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 0px 60px;font-size:20px;line-=
height:28px;background-color:#cfe4ff;text-align:left;font-weight:bold" clas=
s=3D"m_-6107646127073961995subheader1" align=3D"left">BPMN import </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 10px 60px;background-color:#c=
fe4ff;font-size:18px" class=3D"m_-6107646127073961995text1">Import BPMN fil=
es from any other tool into Lucid. Don=E2=80=99t lose your work or your mom=
entum. </td>=20
</tr>=20
<tr>=20
<td>=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%" bgco=
lor=3D"#CFE4FF">=20
<tbody>
<tr>=20
<td width=3D"50" align=3D"center" style=3D"padding:12px 0px 30px 60px" clas=
s=3D"m_-6107646127073961995icon"> <span class=3D"m_-6107646127073961995arw"=
>=E2=9E=94</span> </td>=20
<td style=3D"padding:10px 40px 30px 15px;width:100%;max-width:224px;font-si=
ze:18px;text-align:left" class=3D"m_-6107646127073961995text-CTA"> <a href=
=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh9RxFU4JHtdppQFCISOnH7Pt=
L8m8pEGprZWH_m-N-KoJeslu-ehE-HW9v2rwNqbeoGc=3D" style=3D"color:#282c33;text=
-align:left" class=3D"m_-6107646127073961995link" target=3D"_blank">Get the=
 details</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td align=3D"left" style=3D"padding:40px 60px 20px 60px;background-color:#f=
fffff;vertical-align:top;max-width:100%" class=3D"m_-6107646127073961995sec=
tion-label-pad" valign=3D"top">=20
<div style=3D"padding:1px 10px;background:#282c33;border:1px solid #282c33;=
text-decoration:none;color:#ffffff;border-radius:4px;font-size:16px;font-we=
ight:700">=20
=20
<span>Integrations spotlight</span>=20
=20
</div> </td>=20
</tr>=20
<tr>=20
<td align=3D"center" valign=3D"middle" style=3D"padding:0px 60px 10px 60px;=
background-color:#ffffff" class=3D"m_-6107646127073961995img"> <a href=3D"h=
ttps://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhyhNz9Cg2lWF14DQJWGKIcFbF3weV=
XGPhJJyl9Hq5_1UHV0K1Gqs-Thq3K47e8LC1pM=3D" target=3D"_blank"><img class=3D"=
m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets.lucid=
chart.com/marketing/emails/Newsletters/25-August/Integrations.png" width=3D=
"460" alt=3D"Integrations" style=3D"border:0;width:100%;max-width:460px;ver=
tical-align:middle"></a> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 0px 60px;font-size:20px;line-=
height:28px;background-color:#ffffff;text-align:left;font-weight:bold" clas=
s=3D"m_-6107646127073961995subheader1" align=3D"left">Google Workspace </td=
>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 10px 60px;background-color:#f=
fffff;font-size:18px" class=3D"m_-6107646127073961995text1">Learn how Lucid=
 integrates with Google Workspace, and see an example of what using Lucid a=
nd Google together could look like. </td>=20
</tr>=20
<tr>=20
<td>=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%" bgco=
lor=3D"#FFFFFF">=20
<tbody>
<tr>=20
<td width=3D"50" align=3D"center" style=3D"padding:12px 0px 20px 60px" clas=
s=3D"m_-6107646127073961995icon"> <span class=3D"m_-6107646127073961995arw"=
>=E2=9E=94</span> </td>=20
<td style=3D"padding:10px 40px 20px 15px;width:100%;max-width:224px;font-si=
ze:18px;text-align:left" class=3D"m_-6107646127073961995text-CTA"> <a href=
=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhyhNz9Cg2lWF14DQJWGKIcFb=
F3weVXGPhJJyl9Hq5_1UHV0K1Gqs-Thq3K47e8LC1pM=3D" style=3D"color:#282c33;text=
-align:left" class=3D"m_-6107646127073961995link" target=3D"_blank">Dive de=
eper</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 0px 60px;font-size:20px;line-=
height:28px;background-color:#ffffff;text-align:left;font-weight:bold" clas=
s=3D"m_-6107646127073961995subheader1" align=3D"left">Lucid Cards for Jira =
</td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 10px 60px;background-color:#f=
fffff;font-size:18px" class=3D"m_-6107646127073961995text1">Watch this vide=
o about leveraging Lucid Cards for Jira to visualize planned work, manage t=
asks, and improve team workflows. </td>=20
</tr>=20
<tr>=20
<td>=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%" bgco=
lor=3D"#FFFFFF">=20
<tbody>
<tr>=20
<td width=3D"50" align=3D"center" style=3D"padding:12px 0px 30px 60px" clas=
s=3D"m_-6107646127073961995icon"> <span class=3D"m_-6107646127073961995arw"=
>=E2=9E=94</span> </td>=20
<td style=3D"padding:10px 40px 30px 15px;width:100%;max-width:224px;font-si=
ze:18px;text-align:left" class=3D"m_-6107646127073961995text-CTA"> <a href=
=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mhwETzmrKEi67nczcPRbc98jW=
0AubZuZZSS-S9j55lhLbkbIfhBnHAcmwP7WdbwPW0S4=3D" style=3D"color:#282c33;text=
-align:left" class=3D"m_-6107646127073961995link" target=3D"_blank">Watch n=
ow</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td align=3D"left" style=3D"padding:40px 60px 20px 60px;background-color:#c=
fe4ff;vertical-align:top;max-width:100%" class=3D"m_-6107646127073961995sec=
tion-label-pad" valign=3D"top">=20
<div style=3D"padding:1px 10px;background:#edf5ff;border:1px solid #edf5ff;=
text-decoration:none;color:#1071e5;border-radius:4px;font-size:16px;font-we=
ight:700">=20
=20
<span>Lucid + airfocus</span>=20
=20
</div> </td>=20
</tr>=20
<tr>=20
<td align=3D"center" valign=3D"middle" style=3D"padding:0px 60px 10px 60px;=
background-color:#cfe4ff" class=3D"m_-6107646127073961995img"> <a href=3D"h=
ttps://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_E3Z8hXhcSKp6K-k-4aiZg4lVZqk=
oeKCa3gpOVUqKhBY1KyW26E93bsLgbUJtg9pGg=3D" target=3D"_blank"><img class=3D"=
m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets.lucid=
chart.com/marketing/emails/Newsletters/25-August/airfocus.png" width=3D"460=
" alt=3D"New features" style=3D"border:0;width:100%;max-width:460px;vertica=
l-align:middle"></a> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 0px 60px;font-size:20px;line-=
height:28px;background-color:#cfe4ff;text-align:left;font-weight:bold" clas=
s=3D"m_-6107646127073961995subheader1" align=3D"left">Connected product man=
agement </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 10px 60px;background-color:#c=
fe4ff;font-size:18px" class=3D"m_-6107646127073961995text1">Together, Lucid=
 and airfocus provide a seamless transition from unstructured to structured=
 work. See how product teams benefit from integrating the two platforms. </=
td>=20
</tr>=20
<tr>=20
<td>=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%" bgco=
lor=3D"#CFE4FF">=20
<tbody>
<tr>=20
<td width=3D"50" align=3D"center" style=3D"padding:12px 0px 30px 60px" clas=
s=3D"m_-6107646127073961995icon"> <span class=3D"m_-6107646127073961995arw"=
>=E2=9E=94</span> </td>=20
<td style=3D"padding:10px 40px 30px 15px;width:100%;max-width:224px;font-si=
ze:18px;text-align:left" class=3D"m_-6107646127073961995text-CTA"> <a href=
=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh_E3Z8hXhcSKp6K-k-4aiZg4=
lVZqkoeKCa3gpOVUqKhBY1KyW26E93bsLgbUJtg9pGg=3D" style=3D"color:#282c33;text=
-align:left" class=3D"m_-6107646127073961995link" target=3D"_blank">Learn m=
ore</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td align=3D"left" style=3D"padding:40px 60px 20px 60px;background-color:#f=
fffff;vertical-align:top;max-width:100%" class=3D"m_-6107646127073961995sec=
tion-label-pad" valign=3D"top">=20
<div style=3D"padding:1px 10px;background:#edf5ff;border:1px solid #edf5ff;=
text-decoration:none;color:#1071e5;border-radius:4px;font-size:16px;font-we=
ight:700">=20
=20
<span>Expert tips</span>=20
=20
</div> </td>=20
</tr>=20
<tr>=20
<td style=3D"color:#282c33;background-color:#ffffff">=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%">=20
<tbody>
<tr>=20
<td align=3D"left" valign=3D"top" style=3D"padding:0px 0px 0px 60px;width:1=
20px;max-width:120px" class=3D"m_-6107646127073961995left-col" width=3D"120=
">=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%">=20
<tbody>
<tr>=20
<td width=3D"90" align=3D"left" valign=3D"top" style=3D"padding:0px 0px;wid=
th:90px;max-width:90px" class=3D"m_-6107646127073961995left-image"> <a href=
=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-miB5QY84heCTJE0X22i9Yw6YV=
5Xt6SIDSBEavRh7e8WYLoHrMSdZy85A1_ku9RiWNtWU=3D" target=3D"_blank"> <img cla=
ss=3D"m_-6107646127073961995fadeimg" src=3D"https://cdn-cashy-static-assets=
.lucidchart.com/marketing/emails/Newsletters/25-August/Expert_tip.png" alt=
=3D"Expert tip" border=3D"0" width=3D"90" style=3D"border:0;width:90px;max-=
width:90px;vertical-align:middle"> </a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
<td align=3D"left" valign=3D"middle" style=3D"padding:0px 60px 0px 0px;widt=
h:420px;text-align:left" class=3D"m_-6107646127073961995right-text" width=
=3D"420px">=20
<table cellspacing=3D"0" cellpadding=3D"0" border=3D"0" width=3D"100%">=20
<tbody>
<tr>=20
<td align=3D"left" valign=3D"middle" style=3D"padding:0px 0px;font-weight:b=
old;font-size:20px;text-align:left" class=3D"m_-6107646127073961995subheade=
r1">Prioritization in IT</td>=20
</tr>=20
<tr>=20
<td align=3D"left" valign=3D"top" style=3D"padding:10px 0px 0px 0px;max-wid=
th:224px;font-size:18px" class=3D"m_-6107646127073961995text1">David Torger=
son, Lucid=E2=80=99s VP of infrastructure and IT, recently shared tips for =
prioritizing requests and tasks: =E2=80=9CYou can=E2=80=99t make a good dec=
ision without good data=E2=80=94that=E2=80=99s called guessing.=E2=80=9D He=
 recommends using Lucid integrations to make informed decisions. </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 0px 30px 0px;text-align:left;font-=
size:18px" class=3D"m_-6107646127073961995text-CTA" align=3D"left"> <a href=
=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-miB5QY84heCTJE0X22i9Yw6YV=
5Xt6SIDSBEavRh7e8WYLoHrMSdZy85A1_ku9RiWNtWU=3D" style=3D"color:#282c33;text=
-align:left;font-weight:bold" class=3D"m_-6107646127073961995link" target=
=3D"_blank">Learn more from Torgy</a> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
</tbody>
</table> </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:40px 60px 10px 60px;background-color:#1=
071e5;color:#ffffff;font-size:48px;line-height:52px;text-align:left;font-we=
ight:bold" class=3D"m_-6107646127073961995subheader4" align=3D"left">Most c=
onnected </td>=20
</tr>=20
<tr>=20
<td valign=3D"top" style=3D"padding:10px 60px 20px 60px;color:#ffffff;font-=
size:18px;background-color:#1071e5" class=3D"m_-6107646127073961995text3">W=
hen customers integrate Lucid into their technology ecosystem, they increas=
e everything from collaboration and efficiency to data access and cost savi=
ngs. Contact us to learn about additional integrations available with a Luc=
id Enterprise plan. </td>=20
</tr>=20
<tr>=20
<td align=3D"left" style=3D"padding:10px 60px 60px 60px;font-size:20px;line=
-height:28px;vertical-align:top;background-color:#1071e5" class=3D"m_-61076=
46127073961995button-pad" valign=3D"top">=20
 <a align=3D"center" href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-=
mh1k74SuByYEDdr-WhEommbRig_DyWlQ0QyYvbtll_aJAugaltmK1lILlDpzYVJIPwS8=3D" st=
yle=3D"font-family:Arial,Helvetica,Verdana,sans-serif;font-size:20px;backgr=
ound-color:#282c33;text-decoration:none;padding:.5em 2em;color:#ffffff;disp=
lay:inline-block;border-radius:4px;font-weight:bold" class=3D"m_-6107646127=
073961995button" target=3D"_blank"><span>Talk with sales</span> </a>=20
 </td>=20
</tr>=20
<tr style=3D"background-color:#fafbfc" bgcolor=3D"#FAFBFC">
<td align=3D"left" valign=3D"middle" width=3D"80" height=3D"100%" style=3D"=
font-size:0;padding:35px 24px 0px 60px" class=3D"m_-6107646127073961995logo=
">
<a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-4RYg9CuMxPklsde=
fytSA0ntcNvB9Zs70Kep0oR49VcX2eMXINh6tCxBjYBcPFScHM=3D" target=3D"_blank"><i=
mg src=3D"https://cdn-cashy-static-assets.lucidchart.com/marketing/emails/M=
arketo-Images/Lucid-Primary-Logo-CG100-onClear-np-RGB@2x.png" width=3D"80" =
alt=3D"Lucid" style=3D"border:0;width:80px;max-width:80px;vertical-align:mi=
ddle">
<img src=3D"https://cdn-cashy-static-assets.lucidchart.com/marketing/emails=
/Marketo-Images/Lucid-Primary-Logo-White-onClear-np-RGB@2x.png" width=3D"80=
" alt=3D"Lucid" style=3D"vertical-align:middle;display:none;overflow:hidden=
;float:left;width:0px;max-height:0px;max-width:0px;line-height:0px">
</a>
</td>
</tr>=20
<tr style=3D"background-color:#fafbfc" bgcolor=3D"#FAFBFC">=20
<td style=3D"padding:30px 60px 40px 60px;width:400;font-family:Arial,Helvet=
ica,Verdana,sans-serif;color:#282c33;font-size:12px;line-height:18px" class=
=3D"m_-6107646127073961995footer"><a style=3D"color:#282c33;text-decoration=
:underline" href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh8kYv2iz=
x21Pi8CHlnqUYbKIjV87KD3AviujzB_b2sSaY1sqOkEviHvFE1RsNFoTubE=3D" target=3D"_=
blank">Unsubscribe</a><br><br>=20
Lucid Software Inc.<br>=20
<a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh8nHNOkL5No2g71Nk=
i7g7_fOUAOudHkgqXaVbIJKeDN2N7OjOY_0t9lJZQZ3SVtuYPU=3D" style=3D"text-decora=
tion:none;color:#282c33" target=3D"_blank">10355 South Jordan Gateway, Suit=
e 300<br>=20
South Jordan, UT 84095 USA<br></a><br><br>
By continuing to use Lucid&#39;s products, you agree to our <a href=3D"http=
s://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh-IhXfyW3A21GJGYfVRqXYnABib47OXM=
p7qMGakm_8e5hmfARJp9d_Vcjn2ARIN5IBU=3D" style=3D"color:#282c33;text-decorat=
ion:underline" target=3D"_blank">Terms of Service</a> and acknowledge our <=
a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh3157ebIaPCB6yceTw=
OPKj04w3i8HrHXKgL5IZBHVPBVk6qlJRlNzKk7-16GBoIAICc=3D" style=3D"color:#282c3=
3;text-decoration:underline" target=3D"_blank">Privacy Policy</a>.
  =20
</td>=20
</tr>=20
</tbody>=20
</table>=20
=20
</div>=20
</center> </td>=20
</tr>=20
</tbody>=20
</table>=20
</div>=20

<div id=3D"m_-6107646127073961995_t"></div>=20
<img src=3D"https://ey5xplc8.emltrk.com/v2/ey5xplc8?i=3D165509603" width=3D=
"1" height=3D"1" border=3D"0" alt=3D""> =20
<a href=3D"https://email.lucid.co/NzA0LUJFTC0zNjYAAAGciD-mh0FYk1N5ar0GSqvSR=
uSmNHk-dCRTX0BdH6vNwpWFqimRW0ZcPeqpPMUxQ0EZdN20zFA=3D" target=3D"_blank"></=
a>
<img src=3D"https://email.lucid.co/trk?t=3D1&amp;mid=3DNzA0LUJFTC0zNjYAAAGc=
iD-miDKK4xfyoBk7DHDglocfwQCTdcefm0t6u4Q4Vyc9_qqaK2MxXSIzeOG-mcJGZJgl6v3lTEd=
cOUj28sq1HGZ-FTvgG7B3uy-YZxc-Es2wQM-_A3vJAI1HvvZq6KtxpCKy7vIbV8Q0Yg" width=
=3D"1" height=3D"1" style=3D"display:none!important" alt=3D"">


</div>
</div></div></div>

--0000000000007961c3063d59307a--
"""

real_email_6 = """Delivered-To: ilchenko.evheniia@gmail.com
Received: by 2002:a05:6200:4b89:b0:5b4:106a:d55e with SMTP id dv9csp7629qnb;
        Tue, 12 Aug 2025 18:48:06 -0700 (PDT)
X-Google-Smtp-Source: AGHT+IFv9NGbDf7FaJIWiTVGf6Yk4lx2jprs3i7xG6oPpV0fc/mwB9mIlNkvsp3Z55GDtFhwxJhg
X-Received: by 2002:a05:620a:6082:b0:7e3:3065:a6cf with SMTP id af79cd13be357-7e86522c716mr190981385a.9.1755049685998;
        Tue, 12 Aug 2025 18:48:05 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1755049685; cv=none;
        d=google.com; s=arc-20240605;
        b=B3Pt404rSw5vf44ayzFPdCt/vLeya95TW2gk2lCYSgWD/1whfVO1PItRBqn9RIUV3w
         8eIdLPqfRxgPdB81MffFbdh2FgwPGaCRbjs5nuEA/30EkqO7fZ9llkqOnIsni7wkukRF
         waNNUkspTJbFg7qa69N/BWAOHQn9q6ek+LO21oyEvRLPV2a6T6pHQBjiNgq4i1S7N+iA
         gmqnjRl1xxkuX6ZrwVkS8TzmAF3w2GuGU7UCbO/vnCVYvLXihF/Paf7y/qA6soSVrtJX
         isqSv6Ap0qonrQ6EzLr65XeVjn6dH04hoKlY1TBdXv5ILvpgB1PijHWVfMjd0TYBb37P
         zMCQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;
        h=feedback-id:mime-version:subject:message-id:to:from:date
         :dkim-signature:dkim-signature;
        bh=ldSx8xV+iizj7DsskoOKIKgTLPYk4bGrZutBFrJDlKQ=;
        fh=b26xgq3XgYinM+ZrMdQW71lBAjK2WC3KDt8bU6L0WEk=;
        b=UCAb6Wws+SNGSKK2ZZmMVnRdkMxJlInEfhltfd157j44EGqEJH1bHjE5DFiscKetPX
         K5JnG1pFi6DSnN9k9JRFp4OYrtgCuqkdv2rEKTCOxrMrYg4nYz26njL5bgP5cq9bWUy7
         3H6M013Zg/ds7Qf4E9E5J5MnyE6A0mJ/Tey/lv5ESygWYefZN258mcXtrluy1uk6/MHa
         4AdQfvxheg3nvtCX5SHVbpNTjOOvms9tsIGGw7fhzcvD/dorZ1Ke4R/bsK10qPp2luD8
         OqRZghP27SV6g8BckuBJ5n9h4Cyy/o/Ifn0CsJHYChMM1x2GqBzVj0tGSxOGyahMsHLr
         mJwA==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@amazonaws.com header.s=gjtjdryhn67orwdin77f33td44wkgiw7 header.b=GCnMevHZ;
       dkim=pass header.i=@amazonses.com header.s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw header.b=BpSJjJvc;
       spf=pass (google.com: domain of 01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000@amazonses.com designates 54.240.9.41 as permitted sender) smtp.mailfrom=01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000@amazonses.com;
       dmarc=pass (p=QUARANTINE sp=NONE dis=NONE) header.from=amazonaws.com
Return-Path: <01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000@amazonses.com>
Received: from a9-41.smtp-out.amazonses.com (a9-41.smtp-out.amazonses.com. [54.240.9.41])
        by mx.google.com with ESMTPS id af79cd13be357-7e838af2de1si446340785a.765.2025.08.12.18.48.05
        for <ilchenko.evheniia@gmail.com>
        (version=TLS1_3 cipher=TLS_AES_128_GCM_SHA256 bits=128/128);
        Tue, 12 Aug 2025 18:48:05 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000@amazonses.com designates 54.240.9.41 as permitted sender) client-ip=54.240.9.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@amazonaws.com header.s=gjtjdryhn67orwdin77f33td44wkgiw7 header.b=GCnMevHZ;
       dkim=pass header.i=@amazonses.com header.s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw header.b=BpSJjJvc;
       spf=pass (google.com: domain of 01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000@amazonses.com designates 54.240.9.41 as permitted sender) smtp.mailfrom=01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000@amazonses.com;
       dmarc=pass (p=QUARANTINE sp=NONE dis=NONE) header.from=amazonaws.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=gjtjdryhn67orwdin77f33td44wkgiw7; d=amazonaws.com; t=1755049685;
	h=Date:From:To:Message-ID:Subject:MIME-Version:Content-Type;
	bh=4Btkh8b74ASm7n3dEOCkMZG7Zn3rRvkQ62C9EmqyUDQ=;
	b=GCnMevHZb/UWYQCHzDg6UrMZI/m9TeON0fynAbWNmTXKKpIp5fisyITceqWmM5VU
	zb78eiu1rJwkxUSLq26WktxUw6FmrX53MLVQ1us396/qt4tohq8w9fjNPyeYsIYQEow
	2SdGXdIrwo8PdgIfJeTXB23XYUlKJr23b4m6kCbAj/cio/+hSYkRvCbTJYwkV3j9HX7
	QGn0xGiHseLk3owWpoW/Z3dQMd+fIUo4f9qaTPygPLSatEfT29rfSON9O/9prMxlraM
	MNXoR9wPfBtzJjbR8dO2uT+3SWmpDc1P5+0zf2dKZc+HZA7Te2mvah7sbkX8ZYc9Hz8
	pOXkqCujiA==
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw; d=amazonses.com; t=1755049685;
	h=Date:From:To:Message-ID:Subject:MIME-Version:Content-Type:Feedback-ID;
	bh=4Btkh8b74ASm7n3dEOCkMZG7Zn3rRvkQ62C9EmqyUDQ=;
	b=BpSJjJvcHiZTXd9a5JGM3NfQvoNewbHljlODKeUTN+B3mpoc2t3UHEX2hTNmd0CA
	BuiPUlwBaVCE38/My5Wkq5Tuq7s+VLm+y5jRvsPLUJ5sMs8Rw9Lq/3SOHbYngMugcjP
	PW7Eh8plAhwznfqDoOmz82IL8sO3+qQ5VR0sHNhI=
Date: Wed, 13 Aug 2025 01:48:05 +0000
From: Amazon Web Services <no-reply@amazonaws.com>
To: ilchenko.evheniia@gmail.com
Message-ID: <01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000@email.amazonses.com>
Subject: =?UTF-8?Q?Action_required_=E2=80=93_Your_AWS_account_is_past_due?=
MIME-Version: 1.0
Content-Type: multipart/mixed; 
	boundary="----=_Part_3594627_1391132632.1755049685451"
Feedback-ID: ::1.us-east-1.Rw0MSDPPRrmKml4jfhsJEjYaidP5InuWMFSjPRflgpM=:AmazonSES
X-SES-Outgoing: 2025.08.13-54.240.9.41

------=_Part_3594627_1391132632.1755049685451
Content-Type: multipart/alternative; 
	boundary="----=_Part_3594628_2140175770.1755049685451"

------=_Part_3594628_2140175770.1755049685451
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

<html xmlns=3D"http://www.w3.org/1999/xhtml"><body width=3D"100%" bgcolor=
=3D"#F0F2F3" style=3D"margin: 0;"><center style=3D"width: 100%; background:=
 #F0F2F3; text-align: left;"><div style=3D"margin: auto; max-width: 600px; =
padding-top: 50px;"><!-- Email Header : BEGIN --><table role=3D"presentatio=
n" cellspacing=3D"0" cellpadding=3D"0" border=3D"0" align=3D"center" width=
=3D"100%" id=3D"logoContainer" style=3D"background: #252F3D; border-radius:=
 3px 3px 0 0; max-width: 600px;"><tr>
  <td style=3D"background: #252F3D; border-radius: 3px 3px 0 0; padding: 20=
px 0 10px 0; text-align: center;">
    <a href=3D"https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Faws.=
amazon.com/1/01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000/f=
ae9D3dmWXKbZTHh_56x1PDCHy4=3D439" target=3D"_blank" title=3D"Amazon Web Ser=
vices">
      <img src=3D"https://m.media-amazon.com/images/G/01/amazonwebservices/=
AWS_logo_RGB_REV.png" width=3D"75" height=3D"45" alt=3D"AWS logo" border=3D=
"0" style=3D"font-family: sans-serif; font-size: 15px; line-height: 140%; c=
olor: #555555;">
    </a>
  </td>
</tr></table><!-- Email Header : END --><!-- Email Body : BEGIN --><table r=
ole=3D"presentation" cellspacing=3D"0" cellpadding=3D"0" border=3D"0" align=
=3D"center" width=3D"100%" id=3D"emailBodyContainer" style=3D"border: 0px; =
border-bottom: 1px solid #D6D6D6; max-width: 600px; table-layout:fixed;"><t=
r><td style=3D"background-color: #FFF; color: #444; font-family: 'Amazon Em=
ber', 'Helvetica Neue', Roboto, Arial, sans-serif; font-size: 14px; line-he=
ight: 140%; padding: 25px 35px;"><div><br>
Hello from AWS,<br>
<br>
We recently sent you a reminder about the past due balance on your AWS acco=
unt. This account still has a past due balance.<br>
<br>
Your card payment ending in 1158 failed when we attempted to charge it for =
AWS services on account 851725483987. Please contact your bank to help reso=
lve the payment failure.<br>
<br>
If we are unable to process your payment, your account may be suspended.<br=
>
<br>
Helpful links:<br>
- <a href=3D'https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsol=
e.aws.amazon.com%2Fbilling%2Fhome%23%2Fpaymentsoverview/1/01000198a11cf1d8-=
0475b397-cad6-4855-9fc1-3dfd9207694d-000000/0ITRpjkxgH7X4me720PCBjedT6o=3D4=
39'>Make a payment now</a><br>
- <a href=3D'https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsol=
e.aws.amazon.com%2Fbilling%2Fhome%23%2Fpaymentpreferences/1/01000198a11cf1d=
8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000/GTpEyVpk1y0gifUVC4FQLzibDxU=
=3D439'>Update</a> your default payment method or <a href=3D'https://p6li1c=
hk.r.us-east-1.awstrack.me/L0/https:%2F%2Faws.amazon.com%2Fpremiumsupport%2=
Fknowledge-center%2Fchange-default-payment-method%2F/1/01000198a11cf1d8-047=
5b397-cad6-4855-9fc1-3dfd9207694d-000000/guTQPppgjngQ-qUmmbOpLxcBlzk=3D439'=
>learn more</a> about updating your payment method<br>
- Learn how to <a href=3D'https://p6li1chk.r.us-east-1.awstrack.me/L0/https=
:%2F%2Faws.amazon.com%2Fpremiumsupport%2Fknowledge-center%2Fadd-new-payment=
-method%2F/1/01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000/X=
LsCJI8ZQSgmVM-hd6yGxK7hxvY=3D439'>add</a> a new payment method<br>
<br>
To see your charge details and view the printable PDF copies of your invoic=
es, review the <a href=3D'https://p6li1chk.r.us-east-1.awstrack.me/L0/https=
:%2F%2Fconsole.aws.amazon.com%2Fbilling%2Fhome%3F%23%2Fbills/1/01000198a11c=
f1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000/_nsmQj9-trhFZ0DRS7RIOInyjv=
M=3D439'>AWS Bills</a> console page. If you have any questions, contact <a =
href=3D'https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsole.aws=
.amazon.com%2Fsupport%2Fhome%2F/1/01000198a11cf1d8-0475b397-cad6-4855-9fc1-=
3dfd9207694d-000000/63YFeka8QUeJR0c16Jw3iETuvVI=3D439'>AWS Customer Service=
</a>.<br>
<br>
Thank you,<br>
Amazon Web Services</div><br>
<div><table cellpadding=3D"0" cellspacing=3D"0" border=3D"0" align=3D"cente=
r" style=3D"margin: 0 auto;">
  <tbody>
    <tr>
      <td bgcolor=3D"#232F3E" style=3D"background-color: #232f3e; font-fami=
ly: Helvetica, Arial, sans-serif; color: #ffffff; border: 1px solid #232F3E=
; font-size: 16px; font-weight: 400; text-align: center; vertical-align: to=
p; padding: 16px 25px; line-height: 18px; border-radius: 0px; border-radius=
: 3px;" valign=3D"top">
        <a class=3D"btnLine" style=3D"text-decoration: none; color: #ffffff=
; text-align: center;" target=3D"_blank" href=3D"https://p6li1chk.r.us-east=
-1.awstrack.me/L0/https:%2F%2Fconsole.aws.amazon.com%2Fbilling%2Fhome%23%2F=
paymentsoverview/2/01000198a11cf1d8-0475b397-cad6-4855-9fc1-3dfd9207694d-00=
0000/t-ZMDDk35_XO-NOoLX9plCfY-Z4=3D439">Pay Now</a>
      </td>
    </tr>
  </tbody>
</table></div><br>
</td></tr></table><!-- Email Body : END --><!-- Email Footer : BEGIN --><ta=
ble role=3D"presentation" cellSpacing=3D"0" cellPadding=3D"0" border=3D"0" =
align=3D"center" width=3D"100%" id=3D"footer" style=3D"max-width: 600px;"><=
tr>
  <td style=3D"color: #777; font-family: 'Amazon Ember', 'Helvetica Neue', =
Roboto, Arial, sans-serif; font-size: 12px; line-height: 16px; padding: 20p=
x 25px; text-align: center;">Amazon Web Services, Inc. is a subsidiary of A=
mazon.com, Inc. Amazon.com is a registered trademark of Amazon.com. This me=
ssage was produced and distributed by Amazon Web Services, Inc. or its <a h=
ref=3D"https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Faws.amazon.c=
om%2Flegal%2Fmarketingentities/1/01000198a11cf1d8-0475b397-cad6-4855-9fc1-3=
dfd9207694d-000000/Zq2jNztyRIO_UxUAs6XxFEvsdOk=3D439" style=3D"color: #007e=
b9; text-decoration: none; outline: none;">affiliates</a>, 410 Terry Ave. N=
orth, Seattle, WA 98109. </td>
</tr>
<tr>
  <td style=3D"color: #777; font-family: 'Amazon Ember', 'Helvetica Neue', =
Roboto, Arial, sans-serif; font-size: 12px; line-height: 16px; padding: 5px=
 15px; text-align: center;">=C2=A9 2024, Amazon Web Services, Inc. or its a=
ffiliates. All rights reserved. Read our <a href=3D"https://p6li1chk.r.us-e=
ast-1.awstrack.me/L0/https:%2F%2Faws.amazon.com%2Fprivacy/1/01000198a11cf1d=
8-0475b397-cad6-4855-9fc1-3dfd9207694d-000000/Rapf1jqbgZqfqAjUNJSSDOe__qo=
=3D439" style=3D"color: #007eb9; text-decoration: none; outline: none;">Pri=
vacy Notice</a>. </td>
</tr></table><!-- Email Footer : END --></div></center><img alt=3D"" src=3D=
"https://p6li1chk.r.us-east-1.awstrack.me/I0/01000198a11cf1d8-0475b397-cad6=
-4855-9fc1-3dfd9207694d-000000/1T1jWnrwCPHuLphiPtSXAQYQ-aA=3D439" style=3D"=
display: none; width: 1px; height: 1px;">
</body></html>
------=_Part_3594628_2140175770.1755049685451--

------=_Part_3594627_1391132632.1755049685451--
"""