from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    TECH_VJ_START_TEXT = """
<b>مرحبًا {} 👋

أنا بوت تحميل الروابط

أعطني أي رابط وسأقوم بتحميله كملف أو فيديو مع دعم الصورة المصغرة المخصصة

هذا البوت يعمل بدعم من <a href="https://t.me/X_XF8">المطور</a></b>
"""

    TECH_VJ_HELP_TEXT = """
<b>🖍️ الميزات :-



🔻 ارسل الرابط ثم استرخِ، سيتم تحميل ملفك قريبًا..</b> 
"""

    TECH_VJ_ABOUT_TEXT = """
<b>♻️ اسمي : بوت تحميل الروابط

🌀 القناة : <a href="https://t.me/S_S0F">NETFLIX</a>


👲 المطور : <a href="https://t.me/X_XF8">@X_XF8</a></b>

"""

    
    TECH_VJ_START_BUTTONS = InlineKeyboardMarkup(
        [[
         #   InlineKeyboardButton('💝 اشترك في قناتي على يوتيوب', url='https://youtube.com/@Tech_VJ')
        ], [
            InlineKeyboardButton('🔍 انضم لقناتي !', url='https://t.me/S_S0F'),
            InlineKeyboardButton('🤖 𝑫𝒆𝒗𝒍𝒐𝒑𝒆𝒓', url='https://t.me/X_XF8')
        ], [
            InlineKeyboardButton('❓ مساعدة', callback_data='help'),
            InlineKeyboardButton('🦊 حول', callback_data='about')
        ], [
        #    InlineKeyboardButton('🇮🇳 تابعني على إنستغرام 💖', url='https://instagram.com/tech.vj')
        ]]
    )
    TECH_VJ_HELP_BUTTONS = InlineKeyboardMarkup(
        [[
         #   InlineKeyboardButton('💝 اشترك في قناتي على يوتيوب', url='https://youtube.com/@Tech_VJ')
        ], [
            InlineKeyboardButton('🔍 انضم لقناتي !', url='https://t.me/S_S0F'),
            InlineKeyboardButton('🤖 𝑫𝒆𝒗𝒍𝒐𝒑𝒆𝒓', url='https://t.me/X_XF8')
        ], [
            InlineKeyboardButton('🏠 الرئيسية', callback_data='home'),
            InlineKeyboardButton('🦊 حول', callback_data='about')
        ], [
            InlineKeyboardButton('📛 إغلاق', callback_data='close')
        ]]
    )
    TECH_VJ_ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
         #   InlineKeyboardButton('💝 اشترك في قناتي على يوتيوب', url='https://youtube.com/@Tech_VJ')
        ], [
            InlineKeyboardButton('🔍 انضم لقناتي !', url='https://t.me/S_S0F'),
          #  InlineKeyboardButton('🤖 𝑫𝒆𝒗𝒍𝒐𝒑𝒆𝒓', url='https://t.me/X_XF8')
        ], [
            InlineKeyboardButton('🏠 الرئيسية', callback_data='home'),
            InlineKeyboardButton('❓ مساعدة', callback_data='help')
        ], [
            InlineKeyboardButton('📛 إغلاق', callback_data='close')
        ]]
    )
    
    TECH_VJ_ERROR = "<b>خطأ : {}</b>"

    
    TECH_VJ_FORMAT_SELECTION = "<b>اختر التنسيق المطلوب: قد يكون حجم الملف تقريبيًا \nإذا كنت تريد تعيين صورة مصغرة مخصصة، أرسل الصورة قبل أو بسرعة بعد النقر على أي من الأزرار أدناه.\nيمكنك استخدام /delthumbnail لحذف الصورة المصغرة التي تم إنشاؤها تلقائيًا.</b>"
    TECH_VJ_SET_CUSTOM_USERNAME_PASSWORD = """<b>إذا كنت تريد تحميل مقاطع فيديو مميزة، قدمها بالتنسيق التالي:\nالرابط | اسم الملف | اسم المستخدم | كلمة المرور</b>"""
    TECH_VJ_DOWNLOAD_START = "<b>📥 يتم التحميل...</b>"
    TECH_VJ_UPLOAD_START = "<b>📤 يتم الرفع...</b>"
    TECH_VJ_RCHD_TG_API_LIMIT = "<b>تم التحميل في {} ثانية.\nحجم الملف المكتشف: {}\nعذرًا. لكن، لا يمكنني رفع الملفات التي تزيد عن 2 جيجابايت بسبب قيود واجهة برمجة تطبيقات تيليجرام.</b>"
    TECH_VJ_AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>شكرًا لاستخدامك لي\n\nانضم : @X_XF8</b>"
    TECH_VJ_AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "<b>تم التحميل في {} ثانية.\nتم الرفع في {} ثانية.\n\n@X_XF8</b>"
    TECH_VJ_SAVED_CUSTOM_THUMB_NAIL = "<b>تم حفظ الصورة المصغرة المخصصة للفيديو / الملف. ستتم استخدام هذه الصورة في الفيديو / الملف.</b>"
    TECH_VJ_DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ تم مسح الصورة المصغرة المخصصة بنجاح.</b>"
    TECH_VJ_CUSTOM_CAPTION_UL_FILE = "<b>{}</b>"
    TECH_VJ_NO_VOID_FORMAT_FOUND = "<b>خطأ...\nقال @X_XF8: {}</b>"
    TECH_VJ_REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "<b>رد /generatecustomthumbnail على ألبوم وسائط، لإنشاء صورة مصغرة مخصصة</b>"
    TECH_VJ_ERR_ONLY_TWO_MEDIA_IN_ALBUM = """<b>يجب أن يحتوي ألبوم الوسائط على صورتين فقط. يرجى إعادة إرسال ألبوم الوسائط، ثم حاول مرة أخرى، أو أرسل صورتين فقط في ألبوم.\nيمكنك استخدام الأمر /rename بعد استلام الملف لإعادة تسميته مع دعم الصورة المصغرة المخصصة.</b>"""
    TECH_VJ_CANCEL_STR = "<b>تم إلغاء العملية</b>"
    TECH_VJ_ZIP_UPLOADED_STR = "<b>تم رفع {} ملف في {} ثانية</b>"
    TECH_VJ_SLOW_URL_DECED = "<b>يا إلهي، يبدو أن هذا الرابط بطيء جدًا. بما أنك كنت تشغل بيتي، لست في المزاج لتحميل هذا الملف. أعطني رابطًا سريعًا حتى أتمكن من رفعه إلى تيليجرام، دون أن أبطئ للمستخدمين الآخرين.</b>"

    TECH_VJ_ERROR_YTDLP = "<b>يرجى الإبلاغ عن هذه المشكلة على https://yt-dl.org/bug . تأكد من أنك تستخدم أحدث إصدار؛ راجع https://yt-dl.org/update حول كيفية التحديث. تأكد من استدعاء youtube-dl بعلامة --verbose وقم بتضمين إخراجه الكامل.</b>"
