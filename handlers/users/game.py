from aiogram.types import Message, CallbackQuery
from keyboards.inline.answers_key import key1,key2,key3,key4,key5,key6,key7,key8,key9,key10
from aiogram.dispatcher.filters import Text
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.iqstate import savollar
from aiogram import types
import asyncio



@dp.message_handler(text_contains="Check IQ")
async def savol1(message: Message):
	await message.answer(f"Berilgan so‘zlar ichidan mantiqan ortiqchasini belgilang", reply_markup=key1)
	await savollar.savol1.set()


@dp.callback_query_handler(state=savollar.savol1)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 1
		await state.update_data(var1=s)
		await c.message.answer("Agar bugun shanba bo‘lsa, 29 kundan keyin xaftaning qaysi kuni bo‘ladi?", reply_markup=key2)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol2.set()
	else:
		s = 0
		await state.update_data(var1=s)
		await c.message.answer("Agar bugun shanba bo‘lsa, 29 kundan keyin xaftaning qaysi kuni bo‘ladi?", reply_markup=key2)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol2.set()	


@dp.callback_query_handler(state=savollar.savol2)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 2 
		await state.update_data(var2=s)
		await c.message.answer("Keyingi sonni toping\n6 10 18 34 ?", reply_markup=key3)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol3.set()
	else:
		s = 0
		await state.update_data(var2=s)
		await c.message.answer("Keyingi sonni toping\n6 10 18 34 ?", reply_markup=key3)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol3.set()	


@dp.callback_query_handler(state=savollar.savol3)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 3
		await state.update_data(var3=s)
		await c.message.answer("Bobur ombordan 13 ta stakanda suv olib kelishi kerak. Bir vaqtni o’zida u eng ko’pi 3 ta stakan ko’tara oladi. Bu ishni bajarishi uchun u eng kamida nacha marta borib kelishi kerak.", reply_markup=key4)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol4.set()
	else:
		s = 0
		await state.update_data(var3=s)
		await c.message.answer("Bobur ombordan 13 ta stakanda suv olib kelishi kerak. Bir vaqtni o’zida u eng ko’pi 3 ta stakan ko’tara oladi. Bu ishni bajarishi uchun u eng kamida nacha marta borib kelishi kerak.", reply_markup=key4)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol4.set()


@dp.callback_query_handler(state=savollar.savol4)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 4
		await state.update_data(var4=s)
		await c.message.answer("Ayg’oqchi maxfiy xabarni yuborishga harakat qilmoqda,\nbiz uning xabarini ochishga harakat qilmoqdamiz,\nBiz sizning yordamingizga muhtojmiz!\nAgar (Shnoppy Droppy Groppy)\n(missiya xavfli bajarilgan)\nVa (Swappy Trappy Droppy)\ndegani (darhol missiyani to’xtating)\nVa (Drippy Groppy Wippy)\ndegani (reja muvaffaqiyatli bajarildi) bo’lsa\n'Shnoppy' nimani anglatadi?", reply_markup=key5)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol5.set()
	else:
		s = 0
		await state.update_data(var4=s)
		await c.message.answer("Ayg’oqchi maxfiy xabarni yuborishga harakat qilmoqda,\nbiz uning xabarini ochishga harakat qilmoqdamiz,\nBiz sizning yordamingizga muhtojmiz!\nAgar (Shnoppy Droppy Groppy)\n(missiya xavfli bajarilgan)\nVa (Swappy Trappy Droppy)\ndegani (darhol missiyani to’xtating)\nVa (Drippy Groppy Wippy)\ndegani (reja muvaffaqiyatli bajarildi) bo’lsa\n'Shnoppy' nimani anglatadi?", reply_markup=key5)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol5.set()
	


@dp.callback_query_handler(state=savollar.savol5)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 5
		await state.update_data(var5=s)
		await c.message.answer("Ishchining maoshi dastlab 20% ga, so‘ngra yana 20% ga oshirilgan bo‘lsa, uning maoshi necha foizga oshgan? ", reply_markup=key6)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol6.set()
	else:
		s = 0	
		await state.update_data(var5=s)
		await c.message.answer("Ishchining maoshi dastlab 20% ga, so‘ngra yana 20% ga oshirilgan bo‘lsa, uning maoshi necha foizga oshgan? ", reply_markup=key6)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol6.set()

@dp.callback_query_handler(state=savollar.savol6)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 6
		await state.update_data(var6=s)
		await c.message.answer("Men erkak man. Agar Albertning o’g’li mening o’g’limning otasi bo’lsa. Men va Albertning oramizda qanday qarindoshlik aloqasi bor.", reply_markup=key7)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol7.set()
	else:
		s = 0	
		await state.update_data(var6=s)
		await c.message.answer("Men erkak man. Agar Albertning o’g’li mening o’g’limning otasi bo’lsa. Men va Albertning oramizda qanday qarindoshlik aloqasi bor.", reply_markup=key7)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol7.set()				
		

@dp.callback_query_handler(state=savollar.savol7)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 7
		await state.update_data(var7=s)
		await c.message.answer("Angliyaga amaliyot o‘tash uchun kelgan jami 22 talabaning 12 tasi ingliz tilida, 14 tasi nemis tilida gaplashadi. Qancha talaba ikkala tilda xam so‘zlashadi? ", reply_markup=key8)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol8.set()
	else:
		s = 0
		await state.update_data(var7=s)
		await c.message.answer("Angliyaga amaliyot o‘tash uchun kelgan jami 22 talabaning 12 tasi ingliz tilida, 14 tasi nemis tilida gaplashadi. Qancha talaba ikkala tilda xam so‘zlashadi? ", reply_markup=key8)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol8.set()


@dp.callback_query_handler(state=savollar.savol8)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 8
		await state.update_data(var8=s)
		await c.message.answer("Oilaning 5 nafar a’zolari yoshlari yig‘indisi 78 ga teng. 4 yil avval 61 ga teng bo‘lgan. Oilaning eng kichik a’zosi necha yoshda? ", reply_markup=key9)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol9.set()
	else:
		s = 0
		await state.update_data(var8=s)
		await c.message.answer("Oilaning 5 nafar a’zolari yoshlari yig‘indisi 78 ga teng. 4 yil avval 61 ga teng bo‘lgan. Oilaning eng kichik a’zosi necha yoshda? ", reply_markup=key9)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol9.set()


@dp.callback_query_handler(state=savollar.savol9)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 9
		await state.update_data(var9=s)
		await c.message.answer("Mehmonxona dorixonaga nisbatan ikki kilometr sharqda joylashgan. Bozor esa mehmonxonaga nisbatan bir kilometr g‘arbda joylashgan. Dorixona bozorga nisbatan g‘arbda joylashgan. Agarda dastlabki ikki gap rost bo‘lsa, unda uchinchi gap...", reply_markup=key10)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol10.set()
	else:
		s = 0
		await state.update_data(var9=s)
		await c.message.answer("Mehmonxona dorixonaga nisbatan ikki kilometr sharqda joylashgan. Bozor esa mehmonxonaga nisbatan bir kilometr g‘arbda joylashgan. Dorixona bozorga nisbatan g‘arbda joylashgan. Agarda dastlabki ikki gap rost bo‘lsa, unda uchinchi gap...", reply_markup=key10)
		await c.message.delete()
		await c.answer(cache_time=60)
		await savollar.savol10.set()


@dp.callback_query_handler(state=savollar.savol10)
async def courses(c: CallbackQuery, state: FSMContext):
	if c.data == "True":
		s = 0
		s+= 10
		await state.update_data(var10=s)
		await c.message.delete()
		await c.answer(cache_time=60)
		data = await state.get_data()
		n1 = data.get("var1")
		n2 = data.get("var2")
		n3 = data.get("var3")
		n4 = data.get("var4")
		n5 = data.get("var5")
		n6 = data.get("var6")
		n7 = data.get("var7")
		n8 = data.get("var8")
		n9 = data.get("var9")
		n10 = data.get("var10")
		natija = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
		natija*=2.5
		IQ = int(natija)
		await c.message.answer(f"IQ darajangiz hisoblanmoqda natijani tez orada olasiz")
		await asyncio.sleep(10)
		await c.message.answer("Deyarli tayor 😎")	
		await asyncio.sleep(5)
		await c.message.answer(f"Sizning IQ darajangiz {IQ}")
		await state.reset_state()
	else:
		s = 0
		await state.update_data(var10=s)
		await c.message.delete()
		await c.answer(cache_time=60)
		data = await state.get_data()
		n1 = data.get("var1")
		n2 = data.get("var2")
		n3 = data.get("var3")
		n4 = data.get("var4")
		n5 = data.get("var5")
		n6 = data.get("var6")
		n7 = data.get("var7")
		n8 = data.get("var8")
		n9 = data.get("var9")
		n10 = data.get("var10")
		natija = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
		natija*=2.5
		IQ = int(natija)
		await c.message.answer(f"IQ darajangiz hisoblanmoqda natijani tez orada olasiz")
		await asyncio.sleep(10)
		await c.message.answer("Deyarli tayor 😎")	
		await asyncio.sleep(5)
		await c.message.answer(f"Sizning IQ darajangiz {IQ}")
		await state.reset_state()

		



#data = await state.get_data()
#ism1 = data.get("name1")