from django.test import TestCase

# Create your tests here.
.
├── accounts
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── templates
│   │   └── accounts
│   │       ├── base.html
│   │       ├── frontpage.html
│   │       ├── login.html
│   │       └── signup.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── build
│   └── packaging_script
│       ├── Analysis-00.toc
│       ├── base_library.zip
│       ├── COLLECT-00.toc
│       ├── EXE-00.toc
│       ├── localpycs
│       │   ├── pyimod01_archive.pyc
│       │   ├── pyimod02_importers.pyc
│       │   ├── pyimod03_ctypes.pyc
│       │   └── struct.pyc
│       ├── packaging_script
│       ├── packaging_script.pkg
│       ├── PKG-00.toc
│       ├── PYZ-00.pyz
│       ├── PYZ-00.toc
│       ├── Tree-00.toc
│       ├── Tree-01.toc
│       ├── warn-packaging_script.txt
│       └── xref-packaging_script.html
├── db.sqlite3
├── dist
│   └── packaging_script
│       ├── altgraph-0.17.3.dist-info
│       │   ├── INSTALLER
│       │   ├── LICENSE
│       │   ├── METADATA
│       │   ├── RECORD
│       │   ├── top_level.txt
│       │   ├── WHEEL
│       │   └── zip-safe
│       ├── base_library.zip
│       ├── libBLT.2.5.so.8.6
│       ├── libbrotlicommon.so.1
│       ├── libbrotlidec.so.1
│       ├── libbsd.so.0
│       ├── libbz2.so.1.0
│       ├── libcrypto.so.3
│       ├── lib-dynload
│       │   ├── _asyncio.cpython-310-x86_64-linux-gnu.so
│       │   ├── _bz2.cpython-310-x86_64-linux-gnu.so
│       │   ├── _codecs_cn.cpython-310-x86_64-linux-gnu.so
│       │   ├── _codecs_hk.cpython-310-x86_64-linux-gnu.so
│       │   ├── _codecs_iso2022.cpython-310-x86_64-linux-gnu.so
│       │   ├── _codecs_jp.cpython-310-x86_64-linux-gnu.so
│       │   ├── _codecs_kr.cpython-310-x86_64-linux-gnu.so
│       │   ├── _codecs_tw.cpython-310-x86_64-linux-gnu.so
│       │   ├── _contextvars.cpython-310-x86_64-linux-gnu.so
│       │   ├── _ctypes.cpython-310-x86_64-linux-gnu.so
│       │   ├── _decimal.cpython-310-x86_64-linux-gnu.so
│       │   ├── _hashlib.cpython-310-x86_64-linux-gnu.so
│       │   ├── _json.cpython-310-x86_64-linux-gnu.so
│       │   ├── _lzma.cpython-310-x86_64-linux-gnu.so
│       │   ├── mmap.cpython-310-x86_64-linux-gnu.so
│       │   ├── _multibytecodec.cpython-310-x86_64-linux-gnu.so
│       │   ├── _multiprocessing.cpython-310-x86_64-linux-gnu.so
│       │   ├── _opcode.cpython-310-x86_64-linux-gnu.so
│       │   ├── _posixshmem.cpython-310-x86_64-linux-gnu.so
│       │   ├── _queue.cpython-310-x86_64-linux-gnu.so
│       │   ├── readline.cpython-310-x86_64-linux-gnu.so
│       │   ├── resource.cpython-310-x86_64-linux-gnu.so
│       │   ├── _ssl.cpython-310-x86_64-linux-gnu.so
│       │   ├── termios.cpython-310-x86_64-linux-gnu.so
│       │   └── _tkinter.cpython-310-x86_64-linux-gnu.so
│       ├── libexpat.so.1
│       ├── libffi.so.8
│       ├── libfontconfig.so.1
│       ├── libfreetype.so.6
│       ├── liblzma.so.5
│       ├── libmd.so.0
│       ├── libmpdec.so.3
│       ├── libpng16.so.16
│       ├── libpython3.10.so.1.0
│       ├── libreadline.so.8
│       ├── libssl.so.3
│       ├── libtcl8.6.so
│       ├── libtinfo.so.6
│       ├── libtk8.6.so
│       ├── libuuid.so.1
│       ├── libX11.so.6
│       ├── libXau.so.6
│       ├── libXdmcp.so.6
│       ├── libXext.so.6
│       ├── libXft.so.2
│       ├── libXrender.so.1
│       ├── libXss.so.1
│       ├── libz.so.1
│       ├── packaging_script
│       ├── pyinstaller-5.11.0.dist-info
│       │   ├── COPYING.txt
│       │   ├── entry_points.txt
│       │   ├── INSTALLER
│       │   ├── METADATA
│       │   ├── RECORD
│       │   ├── REQUESTED
│       │   ├── top_level.txt
│       │   └── WHEEL
│       ├── tcl
│       │   ├── auto.tcl
│       │   ├── clock.tcl
│       │   ├── encoding
│       │   │   ├── ascii.enc
│       │   │   ├── big5.enc
│       │   │   ├── cns11643.enc
│       │   │   ├── cp1250.enc
│       │   │   ├── cp1251.enc
│       │   │   ├── cp1252.enc
│       │   │   ├── cp1253.enc
│       │   │   ├── cp1254.enc
│       │   │   ├── cp1255.enc
│       │   │   ├── cp1256.enc
│       │   │   ├── cp1257.enc
│       │   │   ├── cp1258.enc
│       │   │   ├── cp437.enc
│       │   │   ├── cp737.enc
│       │   │   ├── cp775.enc
│       │   │   ├── cp850.enc
│       │   │   ├── cp852.enc
│       │   │   ├── cp855.enc
│       │   │   ├── cp857.enc
│       │   │   ├── cp860.enc
│       │   │   ├── cp861.enc
│       │   │   ├── cp862.enc
│       │   │   ├── cp863.enc
│       │   │   ├── cp864.enc
│       │   │   ├── cp865.enc
│       │   │   ├── cp866.enc
│       │   │   ├── cp869.enc
│       │   │   ├── cp874.enc
│       │   │   ├── cp932.enc
│       │   │   ├── cp936.enc
│       │   │   ├── cp949.enc
│       │   │   ├── cp950.enc
│       │   │   ├── dingbats.enc
│       │   │   ├── ebcdic.enc
│       │   │   ├── euc-cn.enc
│       │   │   ├── euc-jp.enc
│       │   │   ├── euc-kr.enc
│       │   │   ├── gb12345.enc
│       │   │   ├── gb1988.enc
│       │   │   ├── gb2312.enc
│       │   │   ├── gb2312-raw.enc
│       │   │   ├── iso2022.enc
│       │   │   ├── iso2022-jp.enc
│       │   │   ├── iso2022-kr.enc
│       │   │   ├── iso8859-10.enc
│       │   │   ├── iso8859-11.enc
│       │   │   ├── iso8859-13.enc
│       │   │   ├── iso8859-14.enc
│       │   │   ├── iso8859-15.enc
│       │   │   ├── iso8859-16.enc
│       │   │   ├── iso8859-1.enc
│       │   │   ├── iso8859-2.enc
│       │   │   ├── iso8859-3.enc
│       │   │   ├── iso8859-4.enc
│       │   │   ├── iso8859-5.enc
│       │   │   ├── iso8859-6.enc
│       │   │   ├── iso8859-7.enc
│       │   │   ├── iso8859-8.enc
│       │   │   ├── iso8859-9.enc
│       │   │   ├── jis0201.enc
│       │   │   ├── jis0208.enc
│       │   │   ├── jis0212.enc
│       │   │   ├── koi8-r.enc
│       │   │   ├── koi8-u.enc
│       │   │   ├── ksc5601.enc
│       │   │   ├── macCentEuro.enc
│       │   │   ├── macCroatian.enc
│       │   │   ├── macCyrillic.enc
│       │   │   ├── macDingbats.enc
│       │   │   ├── macGreek.enc
│       │   │   ├── macIceland.enc
│       │   │   ├── macJapan.enc
│       │   │   ├── macRoman.enc
│       │   │   ├── macRomania.enc
│       │   │   ├── macThai.enc
│       │   │   ├── macTurkish.enc
│       │   │   ├── macUkraine.enc
│       │   │   ├── shiftjis.enc
│       │   │   ├── symbol.enc
│       │   │   └── tis-620.enc
│       │   ├── history.tcl
│       │   ├── http1.0
│       │   │   ├── http.tcl
│       │   │   └── pkgIndex.tcl
│       │   ├── init.tcl
│       │   ├── msgs
│       │   │   ├── af.msg
│       │   │   ├── af_za.msg
│       │   │   ├── ar_in.msg
│       │   │   ├── ar_jo.msg
│       │   │   ├── ar_lb.msg
│       │   │   ├── ar.msg
│       │   │   ├── ar_sy.msg
│       │   │   ├── be.msg
│       │   │   ├── bg.msg
│       │   │   ├── bn_in.msg
│       │   │   ├── bn.msg
│       │   │   ├── ca.msg
│       │   │   ├── cs.msg
│       │   │   ├── da.msg
│       │   │   ├── de_at.msg
│       │   │   ├── de_be.msg
│       │   │   ├── de.msg
│       │   │   ├── el.msg
│       │   │   ├── en_au.msg
│       │   │   ├── en_be.msg
│       │   │   ├── en_bw.msg
│       │   │   ├── en_ca.msg
│       │   │   ├── en_gb.msg
│       │   │   ├── en_hk.msg
│       │   │   ├── en_ie.msg
│       │   │   ├── en_in.msg
│       │   │   ├── en_nz.msg
│       │   │   ├── en_ph.msg
│       │   │   ├── en_sg.msg
│       │   │   ├── en_za.msg
│       │   │   ├── en_zw.msg
│       │   │   ├── eo.msg
│       │   │   ├── es_ar.msg
│       │   │   ├── es_bo.msg
│       │   │   ├── es_cl.msg
│       │   │   ├── es_co.msg
│       │   │   ├── es_cr.msg
│       │   │   ├── es_do.msg
│       │   │   ├── es_ec.msg
│       │   │   ├── es_gt.msg
│       │   │   ├── es_hn.msg
│       │   │   ├── es.msg
│       │   │   ├── es_mx.msg
│       │   │   ├── es_ni.msg
│       │   │   ├── es_pa.msg
│       │   │   ├── es_pe.msg
│       │   │   ├── es_pr.msg
│       │   │   ├── es_py.msg
│       │   │   ├── es_sv.msg
│       │   │   ├── es_uy.msg
│       │   │   ├── es_ve.msg
│       │   │   ├── et.msg
│       │   │   ├── eu_es.msg
│       │   │   ├── eu.msg
│       │   │   ├── fa_in.msg
│       │   │   ├── fa_ir.msg
│       │   │   ├── fa.msg
│       │   │   ├── fi.msg
│       │   │   ├── fo_fo.msg
│       │   │   ├── fo.msg
│       │   │   ├── fr_be.msg
│       │   │   ├── fr_ca.msg
│       │   │   ├── fr_ch.msg
│       │   │   ├── fr.msg
│       │   │   ├── ga_ie.msg
│       │   │   ├── ga.msg
│       │   │   ├── gl_es.msg
│       │   │   ├── gl.msg
│       │   │   ├── gv_gb.msg
│       │   │   ├── gv.msg
│       │   │   ├── he.msg
│       │   │   ├── hi_in.msg
│       │   │   ├── hi.msg
│       │   │   ├── hr.msg
│       │   │   ├── hu.msg
│       │   │   ├── id_id.msg
│       │   │   ├── id.msg
│       │   │   ├── is.msg
│       │   │   ├── it_ch.msg
│       │   │   ├── it.msg
│       │   │   ├── ja.msg
│       │   │   ├── kl_gl.msg
│       │   │   ├── kl.msg
│       │   │   ├── kok_in.msg
│       │   │   ├── kok.msg
│       │   │   ├── ko_kr.msg
│       │   │   ├── ko.msg
│       │   │   ├── kw_gb.msg
│       │   │   ├── kw.msg
│       │   │   ├── lt.msg
│       │   │   ├── lv.msg
│       │   │   ├── mk.msg
│       │   │   ├── mr_in.msg
│       │   │   ├── mr.msg
│       │   │   ├── ms.msg
│       │   │   ├── ms_my.msg
│       │   │   ├── mt.msg
│       │   │   ├── nb.msg
│       │   │   ├── nl_be.msg
│       │   │   ├── nl.msg
│       │   │   ├── nn.msg
│       │   │   ├── pl.msg
│       │   │   ├── pt_br.msg
│       │   │   ├── pt.msg
│       │   │   ├── ro.msg
│       │   │   ├── ru.msg
│       │   │   ├── ru_ua.msg
│       │   │   ├── sh.msg
│       │   │   ├── sk.msg
│       │   │   ├── sl.msg
│       │   │   ├── sq.msg
│       │   │   ├── sr.msg
│       │   │   ├── sv.msg
│       │   │   ├── sw.msg
│       │   │   ├── ta_in.msg
│       │   │   ├── ta.msg
│       │   │   ├── te_in.msg
│       │   │   ├── te.msg
│       │   │   ├── th.msg
│       │   │   ├── tr.msg
│       │   │   ├── uk.msg
│       │   │   ├── vi.msg
│       │   │   ├── zh_cn.msg
│       │   │   ├── zh_hk.msg
│       │   │   ├── zh.msg
│       │   │   ├── zh_sg.msg
│       │   │   └── zh_tw.msg
│       │   ├── opt0.4
│       │   │   ├── optparse.tcl
│       │   │   └── pkgIndex.tcl
│       │   ├── package.tcl
│       │   ├── parray.tcl
│       │   ├── safe.tcl
│       │   ├── tcl8
│       │   │   ├── http-2.9.5.tm
│       │   │   ├── msgcat-1.6.1.tm
│       │   │   ├── platform
│       │   │   │   └── shell-1.1.4.tm
│       │   │   ├── platform-1.0.18.tm
│       │   │   └── tcltest-2.5.3.tm
│       │   ├── tclAppInit.c
│       │   ├── tclIndex
│       │   ├── tm.tcl
│       │   └── word.tcl
│       ├── tk
│       │   ├── bgerror.tcl
│       │   ├── button.tcl
│       │   ├── choosedir.tcl
│       │   ├── clrpick.tcl
│       │   ├── comdlg.tcl
│       │   ├── console.tcl
│       │   ├── dialog.tcl
│       │   ├── entry.tcl
│       │   ├── focus.tcl
│       │   ├── fontchooser.tcl
│       │   ├── iconlist.tcl
│       │   ├── icons.tcl
│       │   ├── images
│       │   │   ├── logo100.gif
│       │   │   ├── logo64.gif
│       │   │   ├── logo.eps
│       │   │   ├── logoLarge.gif
│       │   │   ├── logoMed.gif
│       │   │   ├── pwrdLogo100.gif
│       │   │   ├── pwrdLogo150.gif
│       │   │   ├── pwrdLogo175.gif
│       │   │   ├── pwrdLogo200.gif
│       │   │   ├── pwrdLogo75.gif
│       │   │   ├── pwrdLogo.eps
│       │   │   ├── README
│       │   │   └── tai-ku.gif
│       │   ├── listbox.tcl
│       │   ├── megawidget.tcl
│       │   ├── menu.tcl
│       │   ├── mkpsenc.tcl
│       │   ├── msgbox.tcl
│       │   ├── msgs
│       │   │   ├── cs.msg
│       │   │   ├── da.msg
│       │   │   ├── de.msg
│       │   │   ├── el.msg
│       │   │   ├── en_gb.msg
│       │   │   ├── en.msg
│       │   │   ├── eo.msg
│       │   │   ├── es.msg
│       │   │   ├── fr.msg
│       │   │   ├── hu.msg
│       │   │   ├── it.msg
│       │   │   ├── nl.msg
│       │   │   ├── pl.msg
│       │   │   ├── pt.msg
│       │   │   ├── ru.msg
│       │   │   └── sv.msg
│       │   ├── obsolete.tcl
│       │   ├── optMenu.tcl
│       │   ├── palette.tcl
│       │   ├── panedwindow.tcl
│       │   ├── safetk.tcl
│       │   ├── scale.tcl
│       │   ├── scrlbar.tcl
│       │   ├── spinbox.tcl
│       │   ├── tclIndex
│       │   ├── tearoff.tcl
│       │   ├── text.tcl
│       │   ├── tkAppInit.c
│       │   ├── tkfbox.tcl
│       │   ├── tk.tcl
│       │   ├── ttk
│       │   │   ├── altTheme.tcl
│       │   │   ├── aquaTheme.tcl
│       │   │   ├── button.tcl
│       │   │   ├── clamTheme.tcl
│       │   │   ├── classicTheme.tcl
│       │   │   ├── combobox.tcl
│       │   │   ├── cursors.tcl
│       │   │   ├── defaults.tcl
│       │   │   ├── entry.tcl
│       │   │   ├── fonts.tcl
│       │   │   ├── menubutton.tcl
│       │   │   ├── notebook.tcl
│       │   │   ├── panedwindow.tcl
│       │   │   ├── progress.tcl
│       │   │   ├── scale.tcl
│       │   │   ├── scrollbar.tcl
│       │   │   ├── sizegrip.tcl
│       │   │   ├── spinbox.tcl
│       │   │   ├── treeview.tcl
│       │   │   ├── ttk.tcl
│       │   │   ├── utils.tcl
│       │   │   ├── vistaTheme.tcl
│       │   │   ├── winTheme.tcl
│       │   │   └── xpTheme.tcl
│       │   ├── unsupported.tcl
│       │   └── xmfbox.tcl
│       └── wheel-0.40.0.dist-info
│           ├── entry_points.txt
│           ├── INSTALLER
│           ├── LICENSE.txt
│           ├── METADATA
│           ├── RECORD
│           └── WHEEL
├── djangochat_core
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── asgi.cpython-310.pyc
│   │   ├── asgi.cpython-39.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── settings.cpython-39.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── utils.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── utils.py
│   └── wsgi.py
├── manage.py
├── packaging_script.py
├── packaging_script.spec
├── requirements.txt
└── room
    ├── admin.py
    ├── apps.py
    ├── consumers.py
    ├── forms.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-310.pyc
    │       ├── __init__.cpython-310.pyc
    │       └── __init__.cpython-39.pyc
    ├── models.py
    ├── __pycache__
    │   ├── admin.cpython-310.pyc
    │   ├── admin.cpython-39.pyc
    │   ├── apps.cpython-310.pyc
    │   ├── apps.cpython-39.pyc
    │   ├── consumers.cpython-310.pyc
    │   ├── consumers.cpython-39.pyc
    │   ├── forms.cpython-310.pyc
    │   ├── __init__.cpython-310.pyc
    │   ├── __init__.cpython-39.pyc
    │   ├── models.cpython-310.pyc
    │   ├── models.cpython-39.pyc
    │   ├── routing.cpython-310.pyc
    │   ├── routing.cpython-39.pyc
    │   ├── urls.cpython-310.pyc
    │   ├── urls.cpython-39.pyc
    │   ├── views.cpython-310.pyc
    │   └── views.cpython-39.pyc
    ├── routing.py
    ├── templates
    │   └── room
    │       ├── create_room.html
    │       ├── room.html
    │       └── rooms.html
    ├── tests.py
    ├── urls.py
    └── views.py

