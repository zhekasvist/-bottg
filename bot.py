import telebot
import sqlite3
import uuid
import random


#=====================
#Менять только эти 2 значения

#Ваш айди в тлеграм
admin_id = 715946691
# токен от бота
token = '1811721715:AAHbtyBTAdo0k3qDe6cJpwoSGdSviP-niJs'
#=====================
bot = telebot.TeleBot(token)
conn_u = sqlite3.connect('udb.sqlite3')
cursor_u = conn_u.cursor()
try: cursor_u.execute('''CREATE TABLE udb (uid text, current_item text, current_price text)''')
except:
	pass
conn_i = sqlite3.connect('items.sqlite3')
cursor_i = conn_i.cursor()
try: cursor_i.execute('''CREATE TABLE items (index_item text, name text, price text)''')
except:
	pass
conn_m = sqlite3.connect('messages.sqlite3')
cursor_m = conn_m.cursor()
try: cursor_m.execute('''CREATE TABLE messages(name text, message_text text)''')
except:
	pass
conn_w = sqlite3.connect('wallets.sqlite3')
cursor_w = conn_w.cursor()
try: cursor_w.execute('''CREATE TABLE wallets(wallet text, acc_number text)''')
except:
	pass
@bot.message_handler(commands=['start_edit'])
def start_message_edit(message):
	try:
		if message.from_user.id == admin_id:
			conn_m = sqlite3.connect('messages.sqlite3')
			cursor_m = conn_m.cursor()
			cursor_m.execute("UPDATE messages SET message_text='"+str(message.text.replace('/start_edit ', ''))+"' WHERE name='start_message'")
			conn_m.commit()
			bot.send_message(message.from_user.id, 'Текст приветсвенного сообщения изменен. Для проверки введите /start')
	except:
		bot.send_message(message.from_user.id, 'Error #1')
@bot.message_handler(commands=['item_edit'])
def item_message_edit(message):
	try:
		if message.from_user.id == admin_id:
			conn_m = sqlite3.connect('messages.sqlite3')
			cursor_m = conn_m.cursor()
			cursor_m.execute("UPDATE messages SET message_text='"+str(message.text.replace('/item_edit ', ''))+"' WHERE name='item_message'")
			conn_m.commit()
			bot.send_message(message.from_user.id, 'Текст сообщения о выборе товара изменен.')
	except:
		bot.send_message(message.from_user.id, 'Error #2')
@bot.message_handler(commands=['pay_edit'])
def pay_message_edit(message):
	try:
		if message.from_user.id == admin_id:
			conn_m = sqlite3.connect('messages.sqlite3')
			cursor_m = conn_m.cursor()
			cursor_m.execute("UPDATE messages SET message_text='"+str(message.text.replace('/pay_edit ', ''))+"' WHERE name='pay_message'")
			conn_m.commit()
			bot.send_message(message.from_user.id, 'Текст сообщения об оплате изменен.')
	except:
		bot.send_message(message.from_user.id, 'Error #3')
@bot.message_handler(commands=['check_edit'])
def check_message_edit(message):
	try:
		if message.from_user.id == admin_id:
			conn_m = sqlite3.connect('messages.sqlite3')
			cursor_m = conn_m.cursor()
			cursor_m.execute("UPDATE messages SET message_text='"+str(message.text.replace('/check_edit ', ''))+"' WHERE name='check_message'")
			conn_m.commit()
			bot.send_message(message.from_user.id, 'Текст сообщения проверки оплаты изменен.')
	except:
		bot.send_message(message.from_user.id, 'Error #4')
@bot.message_handler(commands=['back_edit'])
def back_message_edit(message):
	try:
		if message.from_user.id == admin_id:
			conn_m = sqlite3.connect('messages.sqlite3')
			cursor_m = conn_m.cursor()
			cursor_m.execute("UPDATE messages SET message_text='"+str(message.text.replace('/back_edit ', ''))+"' WHERE name='back_message'")
			conn_m.commit()
			bot.send_message(message.from_user.id, 'Текст сообщения отмены изменен.')
	except:
		bot.send_message(message.from_user.id, 'Error #5')
@bot.message_handler(commands=['add_item'])
def add_item(message):
	try:
		if message.from_user.id == admin_id:
			conn_i = sqlite3.connect('items.sqlite3')
			cursor_i = conn_i.cursor()
			cursor_i.execute("INSERT INTO items VALUES ('"+str(random.randint(111111, 999999))+"', '"+str(message.text.replace('/add_item ', '').split(' | ')[0])+"', '"+str(message.text.replace('/add_item ', '').split(' | ')[1])+"')")
			conn_i.commit()
			bot.send_message(message.from_user.id, 'Товар добавлен! Для обновления товаров нажмите /start')
	except:
		bot.send_message(message.from_user.id, 'Error #6')
@bot.message_handler(commands=['del_item'])
def del_item(message):
	try:
		if message.from_user.id == admin_id:
			conn_i = sqlite3.connect('items.sqlite3')
			cursor_i = conn_i.cursor()
			cursor_i.execute("DELETE FROM items WHERE name='"+str(message.text.replace('/del_item ', ''))+"'")
			conn_i.commit()
			bot.send_message(message.from_user.id, 'Товар удален! Для обновления товаров нажмите /start')
	except:
		bot.send_message(message.from_user.id, 'Error #7')
@bot.message_handler(commands=['check_items'])
def check_items_answer(message):
	try:
		if message.from_user.id == admin_id:
			conn_i = sqlite3.connect('items.sqlite3')
			cursor_i = conn_i.cursor()
			all_items = cursor_i.execute("SELECT * FROM items").fetchall()
			if all_items:
				result = '<code>Список доступных товаров:</code>\n\n'
				for item in all_items:
					result+='🔸<code>Название</code> - ' + str(item[1]) + '\n<code>Цена</code> - ' + str(item[2]) + '\n\n'
				bot.send_message(message.from_user.id, result, parse_mode='HTML')
			else:
				bot.send_message(message.from_user.id, 'Товары отсутствуют...')
	except:
		bot.send_message(message.from_user.id, 'Error #8')
@bot.message_handler(commands=['del_all_items'])
def del_all_items(message):
	try:
		if message.from_user.id == admin_id:
			conn_i = sqlite3.connect('items.sqlite3')
			cursor_i = conn_i.cursor()
			all_items = cursor_i.execute("SELECT * FROM items").fetchall()
			if all_items:
				for item in all_items:
					cursor_i.execute("DELETE FROM items WHERE index_item='"+str(item[0])+"'")
					conn_i.commit()
				bot.send_message(message.from_user.id, 'Все товары удалены!')
	except:
		bot.send_message(message.from_user.id, 'Error #9')
@bot.message_handler(commands=['add_wallet'])
def add_wallet(message):
	try:
		if message.from_user.id == admin_id:
			conn_w = sqlite3.connect('wallets.sqlite3')
			cursor_w = conn_w.cursor()
			cursor_w.execute("INSERT INTO wallets VALUES ('"+str(message.text.replace('/add_wallet ', '').split(' ')[0])+"', '"+str(message.text.replace('/add_wallet ', '').split(' ')[1])+"')")
			conn_w.commit()
			bot.send_message(message.from_user.id, 'Кошелек добавлен!')
	except:
		bot.send_message(message.from_user.id, 'Error #18')		
@bot.message_handler(commands=['del_wallet'])
def del_wallet(message):
	try:
		if message.from_user.id == admin_id:
			conn_w = sqlite3.connect('wallets.sqlite3')
			cursor_w = conn_w.cursor()
			cursor_w.execute("DELETE FROM wallets WHERE wallet='"+str(message.text.replace('/del_wallet ', ''))+"'")
			conn_w.commit()
			bot.send_message(message.from_user.id, 'Кошелек удален!')
	except:
		bot.send_message(message.from_user.id, 'Error #19')
@bot.message_handler(commands=['faq'])
def faq_answer(message):
	try:
		if message.from_user.id == admin_id:
			bot.send_message(message.from_user.id, 'https://telegra.ph/Upravlenie-botom-08-29')
	except:
		bot.send_message(message.from_user.id, 'Error #10')
@bot.message_handler(commands=['start'])
def start_answer(message):
	try:
		conn_u = sqlite3.connect('udb.sqlite3')
		cursor_u = conn_u.cursor()
		conn_i = sqlite3.connect('items.sqlite3')
		cursor_i = conn_i.cursor()
		conn_m = sqlite3.connect('messages.sqlite3')
		cursor_m = conn_m.cursor()
		cursor_u.execute("DELETE FROM udb WHERE uid='"+str(message.from_user.id)+"'")
		cursor_u.execute("INSERT INTO udb VALUES ('"+str(message.from_user.id)+"', 'none', 'none')")
		conn_u.commit()
		start_message_text = cursor_m.execute("SELECT * FROM messages WHERE name='start_message'").fetchall()[0][1]
		ukey = telebot.types.ReplyKeyboardMarkup(True)
		all_items = cursor_i.execute("SELECT * FROM items").fetchall()
		if all_items:
			for item in all_items:
				ukey.row(str(item[1])+' | '+str(item[2]))
			bot.send_message(message.from_user.id, str(start_message_text), parse_mode='HTML', reply_markup=ukey)
		else:
			ukey.row('Товары отсутствуют...')
			bot.send_message(message.from_user.id, str(start_message_text), parse_mode='HTML', reply_markup=ukey)

		if message.from_user.id == admin_id:
			bot.send_message(message.from_user.id, 'Для получения инструкции по управлению ботом напишите /faq\n(это сообщение будете получать только Вы, т.к. у Вас права администратора)')
	except:
		try:bot.send_message(message.from_user.id, 'Error #11')
		except:
			pass
@bot.message_handler(content_types=['text'])
def text_answer(message):
	try:
		conn_u = sqlite3.connect('udb.sqlite3')
		cursor_u = conn_u.cursor()
		conn_i = sqlite3.connect('items.sqlite3')
		cursor_i = conn_i.cursor()
		conn_m = sqlite3.connect('messages.sqlite3')
		cursor_m = conn_m.cursor()
		conn_w = sqlite3.connect('wallets.sqlite3')
		cursor_w = conn_w.cursor()
		all_items = cursor_i.execute("SELECT * FROM items").fetchall()
		if all_items:
			for item in all_items:
				if message.text.startswith(str(item[1])+' | '+str(item[2])):
					try:
						ukey = telebot.types.ReplyKeyboardMarkup(True)
						all_wallets = cursor_w.execute("SELECT * FROM wallets").fetchall()
						if all_wallets:

							for wallet in all_wallets:
								ukey.row(str(wallet[0]))
							ukey.row('↩️ Отменить')
							item_message = str(cursor_m.execute("SELECT * FROM messages WHERE name='item_message'").fetchall()[0][1])
							bot.send_message(message.from_user.id, item_message.format(str(item[1]), str(item[2])), parse_mode='HTML', reply_markup=ukey)
							cursor_u.execute("UPDATE udb SET current_item='"+str(message.text.split(' | ')[0])+"' WHERE uid="+str(message.from_user.id))
							cursor_u.execute("UPDATE udb SET current_price='"+str(message.text.split(' | ')[1])+"' WHERE uid="+str(message.from_user.id))
							conn_u.commit()
						else:
							bot.send_message(message.from_user.id, 'В данный момент кошельки не доступны. Попробуйте позже.')
					except:
						try:bot.send_message(message.from_user.id, 'Error #13')
						except:
							pass
		all_wallets = cursor_w.execute("SELECT * FROM wallets").fetchall()
		if all_wallets:
			for wallet in all_wallets:
				if message.text.startswith(wallet[0]):
					try:
						pay_message = str(cursor_m.execute("SELECT * FROM messages WHERE name='pay_message'").fetchall()[0][1])
						current_item = str(cursor_u.execute("SELECT * FROM udb WHERE uid='"+str(message.from_user.id)+"'").fetchall()[0][1])
						current_price = str(cursor_u.execute("SELECT * FROM udb WHERE uid='"+str(message.from_user.id)+"'").fetchall()[0][2])
						current_wallet = wallet[1]
						ukey = telebot.types.ReplyKeyboardMarkup(True)
						ukey.row('✅ Проверить оплату')
						ukey.row('↩️ Отменить')
						bot.send_message(message.from_user.id, pay_message.format(current_item, message.text, current_wallet, current_price, uuid.uuid4()), parse_mode='HTML', reply_markup=ukey)
					except:
						try:bot.send_message(message.from_user.id, 'Error #18')
						except:
							pass
		if message.text == '✅ Проверить оплату':
			try:
				check_message = str(cursor_m.execute("SELECT * FROM messages WHERE name='check_message'").fetchall()[0][1])
				bot.send_message(message.from_user.id, check_message.format(), parse_mode='HTML')
			except:
				try:bot.send_message(message.from_user.id, 'Error #17')
				except:
					pass
		elif message.text == '↩️ Отменить':
			try:
				back_message_text = cursor_m.execute("SELECT * FROM messages WHERE name='back_message'").fetchall()[0][1]
				ukey = telebot.types.ReplyKeyboardMarkup(True)
				all_items = cursor_i.execute("SELECT * FROM items").fetchall()
				if all_items:
					for item in all_items:
						ukey.row(str(item[1])+' | '+str(item[2]))
				else:
					ukey.row('Товары отсутствуют...')
				bot.send_message(message.from_user.id, str(back_message_text), parse_mode='HTML', reply_markup=ukey)
			except:
				try:bot.send_message(message.from_user.id, 'Error #16')
				except:
					pass
		elif message.text == 'Товары отсутствуют...':
			try:
				back_message_text = cursor_m.execute("SELECT * FROM messages WHERE name='back_message'").fetchall()[0][1]
				ukey = telebot.types.ReplyKeyboardMarkup(True)
				all_items = cursor_i.execute("SELECT * FROM items").fetchall()
				if all_items:
					for item in all_items:
						ukey.row(str(item[1])+' | '+str(item[2]))
				else:
					ukey.row('Товары отсутствуют...')
				bot.send_message(message.from_user.id, str(back_message_text), parse_mode='HTML', reply_markup=ukey)
			except:
				try:bot.send_message(message.from_user.id, 'Error #15')
				except:
					pass
	except:
		try:bot.send_message(message.from_user.id, 'Error #12')
		except:
			pass
bot.polling()