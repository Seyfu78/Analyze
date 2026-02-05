#Load the datasets
customer = pd.read_csv("customer_data.csv")
sales= pd.read_csv("sales_data.csv")
product=pd.read_csv("product_data.csv")
store=pd.read_csv("store_data.csv")


#project
#There could be products that are in the products table but not in the sales table
right_join_a = pd.merge(left = sales , right = product, on = 'product_id' , how = "left", indicator = True)
merged = right_join_a[['customer_id','quantity','discount','list_price','date']]
print(merged.dtypes)
merged = merged.copy()

#parseing
merged['date']=pd.to_datetime(merged['date'])
print(merged.dtypes)
merged['month2'] = merged['date'].dt.month
merged['month']=merged['date'].dt.to_period('M')

merged['discounted_price'] = merged['list_price']*(1-merged['discount'])
print(merged)

#caculating revenue
merged['revenue'] = merged['quantity'] * merged['discounted_price']
merged

monthly_customer_revenue = (merged.groupby(['month', 'customer_id'])['revenue'].sum().reset_index())
monthly_customer_revenue