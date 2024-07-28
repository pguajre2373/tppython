import pandas as pd 
#aqui creamos los data frames 
df1=pd.read_csv("C:/Users/pguajre/Desktop/trabajopython/tppython/ecommerce_customers_dataset.csv",encoding='utf-8')
df2=pd.read_csv("C:/Users/pguajre/Desktop/trabajopython/tppython/ecommerce_order_items_dataset.csv",encoding='utf-8')
df3=pd.read_csv("C:/Users/pguajre/Desktop/trabajopython/tppython/ecommerce_order_payments_dataset.csv",encoding='utf-8')
df4=pd.read_csv("C:/Users/pguajre/Desktop/trabajopython/tppython/ecommerce_orders_dataset.csv",encoding='utf-8')
df5=pd.read_csv("C:/Users/pguajre/Desktop/trabajopython/tppython/ecommerce_products_dataset.csv",encoding='utf-8')

#aqui vamos a establecer el indice como clave primaria 
df1.set_index('customer_id', inplace=True)
df2.set_index('order_id' , inplace=True)
df3.set_index('order_id' , inplace=True)
df4.set_index('order_id' , inplace=True) 
df5.set_index('product_id' ,inplace=True)



clientes_unicos = df1['customer_unique_id'].nunique() 
print("los clientes unicos son:",clientes_unicos)

promedio= df3['payment_value'].mean()
print("promedio de valor de pago por pedido",promedio)

category=df5['product_category_name'].value_counts()
la_mas_repetida=category.idxmax()
print("el producto mas vendido es:", la_mas_repetida) 

total_pedidos=len(df4)
print("el total de pedidos realizados es:", total_pedidos)
