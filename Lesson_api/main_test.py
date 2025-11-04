import sender_stand_request

# 1. Obtener la tabla de usuarios
print("🔍 Obteniendo tabla de usuarios...")
users_response = sender_stand_request.get_users_table()
print("Código de estado:", users_response.status_code)
print("Contenido:")
print(users_response.text)
print("-" * 50)

# 2. Crear un nuevo usuario
print("👤 Creando nuevo usuario...")
new_user_data = {
    "name": "Tony",
    "email": "tony@example.com",
    "password": "segura123"
}
create_response = sender_stand_request.post_new_user(new_user_data)
print("Código de estado:", create_response.status_code)
print("Respuesta JSON:")
print(create_response.json())
print("-" * 50)

# 3. Enviar kits de productos
print("📦 Enviando kits de productos...")
kits_response = sender_stand_request.post_products_kits()
print("Código de estado:", kits_response.status_code)
print("Respuesta JSON:")
print(kits_response.json())
print("-" * 50)

