from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'core_md5', u'md5_cmn', u'Base64Encoding', u'hex_md5', u'safe_add', u'str2binl', u'md5_gg', u'md5_hh', u'md5_ii', u'binl2hex', u'bit_rol', u'utf8_encode', u'md5_ff'])
@Js
def PyJsHoisted_core_md5_(x, len, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments, u'len':len}, var)
    var.registers([u'a', u'c', u'b', u'd', u'i', u'len', u'olda', u'oldc', u'oldb', u'oldd', u'x'])
    var.get(u'x').put((var.get(u'len')>>Js(5.0)), (Js(128)<<(var.get(u'len')%Js(32.0))), u'|')
    var.get(u'x').put(((PyJsBshift((var.get(u'len')+Js(64.0)),Js(9.0))<<Js(4.0))+Js(14.0)), var.get(u'len'))
    var.put(u'a', Js(1732584193.0))
    var.put(u'b', (-Js(271733879.0)))
    var.put(u'c', (-Js(1732584194.0)))
    var.put(u'd', Js(271733878.0))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<var.get(u'x').get(u'length')):
        try:
            var.put(u'olda', var.get(u'a'))
            var.put(u'oldb', var.get(u'b'))
            var.put(u'oldc', var.get(u'c'))
            var.put(u'oldd', var.get(u'd'))
            var.put(u'a', var.get(u'md5_ff')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(0.0))), Js(7.0), (-Js(680876936.0))))
            var.put(u'd', var.get(u'md5_ff')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(1.0))), Js(12.0), (-Js(389564586.0))))
            var.put(u'c', var.get(u'md5_ff')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(2.0))), Js(17.0), Js(606105819.0)))
            var.put(u'b', var.get(u'md5_ff')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(3.0))), Js(22.0), (-Js(1044525330.0))))
            var.put(u'a', var.get(u'md5_ff')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(4.0))), Js(7.0), (-Js(176418897.0))))
            var.put(u'd', var.get(u'md5_ff')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(5.0))), Js(12.0), Js(1200080426.0)))
            var.put(u'c', var.get(u'md5_ff')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(6.0))), Js(17.0), (-Js(1473231341.0))))
            var.put(u'b', var.get(u'md5_ff')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(7.0))), Js(22.0), (-Js(45705983.0))))
            var.put(u'a', var.get(u'md5_ff')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(8.0))), Js(7.0), Js(1770035416.0)))
            var.put(u'd', var.get(u'md5_ff')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(9.0))), Js(12.0), (-Js(1958414417.0))))
            var.put(u'c', var.get(u'md5_ff')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(10.0))), Js(17.0), (-Js(42063.0))))
            var.put(u'b', var.get(u'md5_ff')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(11.0))), Js(22.0), (-Js(1990404162.0))))
            var.put(u'a', var.get(u'md5_ff')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(12.0))), Js(7.0), Js(1804603682.0)))
            var.put(u'd', var.get(u'md5_ff')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(13.0))), Js(12.0), (-Js(40341101.0))))
            var.put(u'c', var.get(u'md5_ff')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(14.0))), Js(17.0), (-Js(1502002290.0))))
            var.put(u'b', var.get(u'md5_ff')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(15.0))), Js(22.0), Js(1236535329.0)))
            var.put(u'a', var.get(u'md5_gg')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(1.0))), Js(5.0), (-Js(165796510.0))))
            var.put(u'd', var.get(u'md5_gg')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(6.0))), Js(9.0), (-Js(1069501632.0))))
            var.put(u'c', var.get(u'md5_gg')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(11.0))), Js(14.0), Js(643717713.0)))
            var.put(u'b', var.get(u'md5_gg')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(0.0))), Js(20.0), (-Js(373897302.0))))
            var.put(u'a', var.get(u'md5_gg')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(5.0))), Js(5.0), (-Js(701558691.0))))
            var.put(u'd', var.get(u'md5_gg')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(10.0))), Js(9.0), Js(38016083.0)))
            var.put(u'c', var.get(u'md5_gg')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(15.0))), Js(14.0), (-Js(660478335.0))))
            var.put(u'b', var.get(u'md5_gg')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(4.0))), Js(20.0), (-Js(405537848.0))))
            var.put(u'a', var.get(u'md5_gg')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(9.0))), Js(5.0), Js(568446438.0)))
            var.put(u'd', var.get(u'md5_gg')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(14.0))), Js(9.0), (-Js(1019803690.0))))
            var.put(u'c', var.get(u'md5_gg')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(3.0))), Js(14.0), (-Js(187363961.0))))
            var.put(u'b', var.get(u'md5_gg')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(8.0))), Js(20.0), Js(1163531501.0)))
            var.put(u'a', var.get(u'md5_gg')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(13.0))), Js(5.0), (-Js(1444681467.0))))
            var.put(u'd', var.get(u'md5_gg')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(2.0))), Js(9.0), (-Js(51403784.0))))
            var.put(u'c', var.get(u'md5_gg')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(7.0))), Js(14.0), Js(1735328473.0)))
            var.put(u'b', var.get(u'md5_gg')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(12.0))), Js(20.0), (-Js(1926607734.0))))
            var.put(u'a', var.get(u'md5_hh')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(5.0))), Js(4.0), (-Js(378558.0))))
            var.put(u'd', var.get(u'md5_hh')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(8.0))), Js(11.0), (-Js(2022574463.0))))
            var.put(u'c', var.get(u'md5_hh')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(11.0))), Js(16.0), Js(1839030562.0)))
            var.put(u'b', var.get(u'md5_hh')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(14.0))), Js(23.0), (-Js(35309556.0))))
            var.put(u'a', var.get(u'md5_hh')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(1.0))), Js(4.0), (-Js(1530992060.0))))
            var.put(u'd', var.get(u'md5_hh')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(4.0))), Js(11.0), Js(1272893353.0)))
            var.put(u'c', var.get(u'md5_hh')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(7.0))), Js(16.0), (-Js(155497632.0))))
            var.put(u'b', var.get(u'md5_hh')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(10.0))), Js(23.0), (-Js(1094730640.0))))
            var.put(u'a', var.get(u'md5_hh')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(13.0))), Js(4.0), Js(681279174.0)))
            var.put(u'd', var.get(u'md5_hh')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(0.0))), Js(11.0), (-Js(358537222.0))))
            var.put(u'c', var.get(u'md5_hh')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(3.0))), Js(16.0), (-Js(722521979.0))))
            var.put(u'b', var.get(u'md5_hh')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(6.0))), Js(23.0), Js(76029189.0)))
            var.put(u'a', var.get(u'md5_hh')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(9.0))), Js(4.0), (-Js(640364487.0))))
            var.put(u'd', var.get(u'md5_hh')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(12.0))), Js(11.0), (-Js(421815835.0))))
            var.put(u'c', var.get(u'md5_hh')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(15.0))), Js(16.0), Js(530742520.0)))
            var.put(u'b', var.get(u'md5_hh')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(2.0))), Js(23.0), (-Js(995338651.0))))
            var.put(u'a', var.get(u'md5_ii')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(0.0))), Js(6.0), (-Js(198630844.0))))
            var.put(u'd', var.get(u'md5_ii')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(7.0))), Js(10.0), Js(1126891415.0)))
            var.put(u'c', var.get(u'md5_ii')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(14.0))), Js(15.0), (-Js(1416354905.0))))
            var.put(u'b', var.get(u'md5_ii')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(5.0))), Js(21.0), (-Js(57434055.0))))
            var.put(u'a', var.get(u'md5_ii')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(12.0))), Js(6.0), Js(1700485571.0)))
            var.put(u'd', var.get(u'md5_ii')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(3.0))), Js(10.0), (-Js(1894986606.0))))
            var.put(u'c', var.get(u'md5_ii')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(10.0))), Js(15.0), (-Js(1051523.0))))
            var.put(u'b', var.get(u'md5_ii')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(1.0))), Js(21.0), (-Js(2054922799.0))))
            var.put(u'a', var.get(u'md5_ii')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(8.0))), Js(6.0), Js(1873313359.0)))
            var.put(u'd', var.get(u'md5_ii')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(15.0))), Js(10.0), (-Js(30611744.0))))
            var.put(u'c', var.get(u'md5_ii')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(6.0))), Js(15.0), (-Js(1560198380.0))))
            var.put(u'b', var.get(u'md5_ii')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(13.0))), Js(21.0), Js(1309151649.0)))
            var.put(u'a', var.get(u'md5_ii')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'x').get((var.get(u'i')+Js(4.0))), Js(6.0), (-Js(145523070.0))))
            var.put(u'd', var.get(u'md5_ii')(var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'x').get((var.get(u'i')+Js(11.0))), Js(10.0), (-Js(1120210379.0))))
            var.put(u'c', var.get(u'md5_ii')(var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'b'), var.get(u'x').get((var.get(u'i')+Js(2.0))), Js(15.0), Js(718787259.0)))
            var.put(u'b', var.get(u'md5_ii')(var.get(u'b'), var.get(u'c'), var.get(u'd'), var.get(u'a'), var.get(u'x').get((var.get(u'i')+Js(9.0))), Js(21.0), (-Js(343485551.0))))
            var.put(u'a', var.get(u'safe_add')(var.get(u'a'), var.get(u'olda')))
            var.put(u'b', var.get(u'safe_add')(var.get(u'b'), var.get(u'oldb')))
            var.put(u'c', var.get(u'safe_add')(var.get(u'c'), var.get(u'oldc')))
            var.put(u'd', var.get(u'safe_add')(var.get(u'd'), var.get(u'oldd')))
        finally:
                var.put(u'i', Js(16.0), u'+')
    return var.get(u'Array')(var.get(u'a'), var.get(u'b'), var.get(u'c'), var.get(u'd'))
PyJsHoisted_core_md5_.func_name = u'core_md5'
var.put(u'core_md5', PyJsHoisted_core_md5_)
@Js
def PyJsHoisted_md5_cmn_(q, a, b, x, s, t, this, arguments, var=var):
    var = Scope({u'a':a, u'b':b, u'this':this, u'q':q, u's':s, u't':t, u'x':x, u'arguments':arguments}, var)
    var.registers([u'a', u'b', u'q', u's', u't', u'x'])
    return var.get(u'safe_add')(var.get(u'bit_rol')(var.get(u'safe_add')(var.get(u'safe_add')(var.get(u'a'), var.get(u'q')), var.get(u'safe_add')(var.get(u'x'), var.get(u't'))), var.get(u's')), var.get(u'b'))
PyJsHoisted_md5_cmn_.func_name = u'md5_cmn'
var.put(u'md5_cmn', PyJsHoisted_md5_cmn_)
@Js
def PyJsHoisted_Base64Encoding_(input, this, arguments, var=var):
    var = Scope({u'this':this, u'input':input, u'arguments':arguments}, var)
    var.registers([u'chr3', u'chr2', u'chr1', u'i', u'enc4', u'keyStr', u'enc1', u'enc2', u'enc3', u'output', u'input'])
    var.put(u'keyStr', Js(u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='))
    var.put(u'output', Js(u''))
    pass
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<var.get(u'input').get(u'length')):
        var.put(u'chr1', var.get(u'input').callprop(u'charCodeAt', (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        var.put(u'chr2', var.get(u'input').callprop(u'charCodeAt', (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        var.put(u'chr3', var.get(u'input').callprop(u'charCodeAt', (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        var.put(u'enc1', (var.get(u'chr1')>>Js(2.0)))
        var.put(u'enc2', (((var.get(u'chr1')&Js(3.0))<<Js(4.0))|(var.get(u'chr2')>>Js(4.0))))
        var.put(u'enc3', (((var.get(u'chr2')&Js(15.0))<<Js(2.0))|(var.get(u'chr3')>>Js(6.0))))
        var.put(u'enc4', (var.get(u'chr3')&Js(63.0)))
        if var.get(u'isNaN')(var.get(u'chr2')):
            var.put(u'enc3', var.put(u'enc4', Js(64.0)))
        else:
            if var.get(u'isNaN')(var.get(u'chr3')):
                var.put(u'enc4', Js(64.0))
        var.put(u'output', ((((var.get(u'output')+var.get(u'keyStr').callprop(u'charAt', var.get(u'enc1')))+var.get(u'keyStr').callprop(u'charAt', var.get(u'enc2')))+var.get(u'keyStr').callprop(u'charAt', var.get(u'enc3')))+var.get(u'keyStr').callprop(u'charAt', var.get(u'enc4'))))
    return var.get(u'output')
PyJsHoisted_Base64Encoding_.func_name = u'Base64Encoding'
var.put(u'Base64Encoding', PyJsHoisted_Base64Encoding_)
@Js
def PyJsHoisted_hex_md5_(s, this, arguments, var=var):
    var = Scope({u'this':this, u's':s, u'arguments':arguments}, var)
    var.registers([u's'])
    return var.get(u'binl2hex')(var.get(u'core_md5')(var.get(u'str2binl')(var.get(u's')), (var.get(u's').get(u'length')*Js(8.0))))
PyJsHoisted_hex_md5_.func_name = u'hex_md5'
var.put(u'hex_md5', PyJsHoisted_hex_md5_)
@Js
def PyJsHoisted_safe_add_(x, y, this, arguments, var=var):
    var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments}, var)
    var.registers([u'msw', u'lsw', u'y', u'x'])
    var.put(u'lsw', ((var.get(u'x')&Js(65535))+(var.get(u'y')&Js(65535))))
    var.put(u'msw', (((var.get(u'x')>>Js(16.0))+(var.get(u'y')>>Js(16.0)))+(var.get(u'lsw')>>Js(16.0))))
    return ((var.get(u'msw')<<Js(16.0))|(var.get(u'lsw')&Js(65535)))
PyJsHoisted_safe_add_.func_name = u'safe_add'
var.put(u'safe_add', PyJsHoisted_safe_add_)
@Js
def PyJsHoisted_str2binl_(str, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'str':str}, var)
    var.registers([u'bin', u'i', u'mask', u'str'])
    var.put(u'bin', var.get(u'Array')())
    var.put(u'mask', ((Js(1.0)<<Js(8.0))-Js(1.0)))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<(var.get(u'str').get(u'length')*Js(8.0))):
        try:
            var.get(u'bin').put((var.get(u'i')>>Js(5.0)), ((var.get(u'str').callprop(u'charCodeAt', (var.get(u'i')/Js(8.0)))&var.get(u'mask'))<<(var.get(u'i')%Js(32.0))), u'|')
        finally:
                var.put(u'i', Js(8.0), u'+')
    return var.get(u'bin')
PyJsHoisted_str2binl_.func_name = u'str2binl'
var.put(u'str2binl', PyJsHoisted_str2binl_)
@Js
def PyJsHoisted_md5_gg_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({u'a':a, u'c':c, u'b':b, u'd':d, u'this':this, u's':s, u't':t, u'x':x, u'arguments':arguments}, var)
    var.registers([u'a', u'c', u'b', u'd', u's', u't', u'x'])
    return var.get(u'md5_cmn')(((var.get(u'b')&var.get(u'd'))|(var.get(u'c')&(~var.get(u'd')))), var.get(u'a'), var.get(u'b'), var.get(u'x'), var.get(u's'), var.get(u't'))
PyJsHoisted_md5_gg_.func_name = u'md5_gg'
var.put(u'md5_gg', PyJsHoisted_md5_gg_)
@Js
def PyJsHoisted_md5_hh_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({u'a':a, u'c':c, u'b':b, u'd':d, u'this':this, u's':s, u't':t, u'x':x, u'arguments':arguments}, var)
    var.registers([u'a', u'c', u'b', u'd', u's', u't', u'x'])
    return var.get(u'md5_cmn')(((var.get(u'b')^var.get(u'c'))^var.get(u'd')), var.get(u'a'), var.get(u'b'), var.get(u'x'), var.get(u's'), var.get(u't'))
PyJsHoisted_md5_hh_.func_name = u'md5_hh'
var.put(u'md5_hh', PyJsHoisted_md5_hh_)
@Js
def PyJsHoisted_md5_ii_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({u'a':a, u'c':c, u'b':b, u'd':d, u'this':this, u's':s, u't':t, u'x':x, u'arguments':arguments}, var)
    var.registers([u'a', u'c', u'b', u'd', u's', u't', u'x'])
    return var.get(u'md5_cmn')((var.get(u'c')^(var.get(u'b')|(~var.get(u'd')))), var.get(u'a'), var.get(u'b'), var.get(u'x'), var.get(u's'), var.get(u't'))
PyJsHoisted_md5_ii_.func_name = u'md5_ii'
var.put(u'md5_ii', PyJsHoisted_md5_ii_)
@Js
def PyJsHoisted_binl2hex_(binarray, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'binarray':binarray}, var)
    var.registers([u'hex_tab', u'i', u'binarray', u'str'])
    var.put(u'hex_tab', Js(u'0123456789abcdef'))
    var.put(u'str', Js(u''))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<(var.get(u'binarray').get(u'length')*Js(4.0))):
        try:
            var.put(u'str', (var.get(u'hex_tab').callprop(u'charAt', ((var.get(u'binarray').get((var.get(u'i')>>Js(2.0)))>>(((var.get(u'i')%Js(4.0))*Js(8.0))+Js(4.0)))&Js(15)))+var.get(u'hex_tab').callprop(u'charAt', ((var.get(u'binarray').get((var.get(u'i')>>Js(2.0)))>>((var.get(u'i')%Js(4.0))*Js(8.0)))&Js(15)))), u'+')
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    return var.get(u'str')
PyJsHoisted_binl2hex_.func_name = u'binl2hex'
var.put(u'binl2hex', PyJsHoisted_binl2hex_)
@Js
def PyJsHoisted_bit_rol_(num, cnt, this, arguments, var=var):
    var = Scope({u'this':this, u'cnt':cnt, u'num':num, u'arguments':arguments}, var)
    var.registers([u'cnt', u'num'])
    return ((var.get(u'num')<<var.get(u'cnt'))|PyJsBshift(var.get(u'num'),(Js(32.0)-var.get(u'cnt'))))
PyJsHoisted_bit_rol_.func_name = u'bit_rol'
var.put(u'bit_rol', PyJsHoisted_bit_rol_)
@Js
def PyJsHoisted_utf8_encode_(string, this, arguments, var=var):
    var = Scope({u'this':this, u'string':string, u'arguments':arguments}, var)
    var.registers([u'c', u'utftext', u'string', u'n'])
    var.put(u'string', var.get(u'string').callprop(u'replace', JsRegExp(u'/\\r\\n/g'), Js(u'\n')))
    var.put(u'utftext', Js(u''))
    #for JS loop
    var.put(u'n', Js(0.0))
    while (var.get(u'n')<var.get(u'string').get(u'length')):
        try:
            var.put(u'c', var.get(u'string').callprop(u'charCodeAt', var.get(u'n')))
            if (var.get(u'c')<Js(128.0)):
                var.put(u'utftext', var.get(u'String').callprop(u'fromCharCode', var.get(u'c')), u'+')
            else:
                if ((var.get(u'c')>Js(127.0)) and (var.get(u'c')<Js(2048.0))):
                    var.put(u'utftext', var.get(u'String').callprop(u'fromCharCode', ((var.get(u'c')>>Js(6.0))|Js(192.0))), u'+')
                    var.put(u'utftext', var.get(u'String').callprop(u'fromCharCode', ((var.get(u'c')&Js(63.0))|Js(128.0))), u'+')
                else:
                    var.put(u'utftext', var.get(u'String').callprop(u'fromCharCode', ((var.get(u'c')>>Js(12.0))|Js(224.0))), u'+')
                    var.put(u'utftext', var.get(u'String').callprop(u'fromCharCode', (((var.get(u'c')>>Js(6.0))&Js(63.0))|Js(128.0))), u'+')
                    var.put(u'utftext', var.get(u'String').callprop(u'fromCharCode', ((var.get(u'c')&Js(63.0))|Js(128.0))), u'+')
        finally:
                (var.put(u'n',Js(var.get(u'n').to_number())+Js(1))-Js(1))
    return var.get(u'utftext')
PyJsHoisted_utf8_encode_.func_name = u'utf8_encode'
var.put(u'utf8_encode', PyJsHoisted_utf8_encode_)
@Js
def PyJsHoisted_md5_ff_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({u'a':a, u'c':c, u'b':b, u'd':d, u'this':this, u's':s, u't':t, u'x':x, u'arguments':arguments}, var)
    var.registers([u'a', u'c', u'b', u'd', u's', u't', u'x'])
    return var.get(u'md5_cmn')(((var.get(u'b')&var.get(u'c'))|((~var.get(u'b'))&var.get(u'd'))), var.get(u'a'), var.get(u'b'), var.get(u'x'), var.get(u's'), var.get(u't'))
PyJsHoisted_md5_ff_.func_name = u'md5_ff'
var.put(u'md5_ff', PyJsHoisted_md5_ff_)
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
