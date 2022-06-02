# pip install streamlit fbprophet yfinance plotly
import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2010-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
st.button('السوق السعودي')
st.button('السوق الامريكي')
st.button('الفوركس')


#st.title('توقع حركة السوق السعودي')
html_string = "<h1 style='text-align: center; color: balck;'>توقع حركة السوق السعودي</h1>"

st.markdown(html_string, unsafe_allow_html=True)

stocks = ("1010.SR",
"1020.SR",
"1030.SR",
"1050.SR",
"1060.SR",
"1080.SR",
"1111.SR",
"1120.SR",
"1140.SR",
"1150.SR",
"1180.SR",
"1182.SR",
"1183.SR",
"1201.SR",
"1202.SR",
"1210.SR",
"1211.SR",
"1212.SR",
"1213.SR",
"1214.SR",
"1301.SR",
"1302.SR",
"1303.SR",
"1304.SR",
"1320.SR",
"1321.SR",
"1322.SR",
"1810.SR",
"1820.SR",
"1830.SR",
"1831.SR",
"1832.SR",
"2001.SR",
"2002.SR",
"2010.SR",
"2020.SR",
"2030.SR",
"2040.SR",
"2050.SR",
"2060.SR",
"2070.SR",
"2080.SR",
"2081.SR",
"2082.SR",
"2090.SR",
"2100.SR",
"2110.SR",
"2120.SR",
"2130.SR",
"2140.SR",
"2150.SR",
"2160.SR",
"2170.SR",
"2180.SR",
"2190.SR",
"2200.SR",
"2210.SR",
"2220.SR",
"2222.SR",
"2230.SR",
"2240.SR",
"2250.SR",
"2270.SR",
"2280.SR",
"2281.SR",
"2290.SR",
"2300.SR",
"2310.SR",
"2320.SR",
"2330.SR",
"2340.SR",
"2350.SR",
"2360.SR",
"2370.SR",
"2380.SR",
"3001.SR",
"3002.SR",
"3003.SR",
"3004.SR",
"3005.SR",
"3007.SR",
"3008.SR",
"3010.SR",
"3020.SR",
"3030.SR",
"3040.SR",
"3050.SR",
"3060.SR",
"3080.SR",
"3090.SR",
"3091.SR",
"4001.SR",
"4002.SR",
"4003.SR",
"4004.SR",
"4005.SR",
"4006.SR",
"4007.SR",
"4008.SR",
"4009.SR",
"4010.SR",
"4011.SR",
"4012.SR",
"4013.SR",
"4014.SR",
"4020.SR",
"4030.SR",
"4031.SR",
"4040.SR",
"4050.SR",
"4051.SR",
"4061.SR",
"4070.SR",
"4071.SR",
"4080.SR",
"4081.SR",
"4090.SR",
"4100.SR",
"4110.SR",
"4130.SR",
"4140.SR",
"4141.SR",
"4150.SR",
"4160.SR",
"4161.SR",
"4162.SR",
"4163.SR",
"4164.SR",
"4170.SR",
"4180.SR",
"4190.SR",
"4191.SR",
"4200.SR",
"4210.SR",
"4220.SR",
"4230.SR",
"4240.SR",
"4250.SR",
"4260.SR",
"4261.SR",
"4270.SR",
"4280.SR",
"4290.SR",
"4291.SR",
"4292.SR",
"4300.SR",
"4310.SR",
"4320.SR",
"4321.SR",
"4330.SR",
"4331.SR",
"4332.SR",
"4333.SR",
"4334.SR",
"4335.SR",
"4336.SR",
"4337.SR",
"4338.SR",
"4339.SR",
"4340.SR",
"4342.SR",
"4344.SR",
"4345.SR",
"4346.SR",
"4347.SR",
"4348.SR",
"4700.SR",
"4701.SR",
"5110.SR",
"6001.SR",
"6002.SR",
"6004.SR",
"6010.SR",
"6012.SR",
"6013.SR",
"6020.SR",
"6040.SR",
"6050.SR",
"6060.SR",
"6070.SR",
"6090.SR",
"7010.SR",
"7020.SR",
"7030.SR",
"7040.SR",
"7200.SR",
"7201.SR",
"7202.SR",
"7203.SR",
"8010.SR",
"8012.SR",
"8020.SR",
"8030.SR",
"8040.SR",
"8050.SR",
"8060.SR",
"8070.SR",
"8080.SR",
"8100.SR",
"8110.SR",
"8120.SR",
"8130.SR",
"8150.SR",
"8160.SR",
"8170.SR",
"8180.SR",
"8190.SR",
"8200.SR",
"8210.SR",
"8230.SR",
"8240.SR",
"8250.SR",
"8260.SR",
"8270.SR",
"8280.SR",
"8300.SR",
"83002.SR",
"8310.SR",
"8311.SR",
"8312.SR",
"9400.SR",
"9401.SR",
"9402.SR",
"9403.SR",
"9404.SR",
"9405.SR",
"9406.SR",
"9510.SR",
"9511.SR",
"9512.SR",
"9513.SR",
"9514.SR",
"9515.SR",
"9516.SR",
"9517.SR",
"9518.SR",
"9519.SR",
"9520.SR",
"9521.SR",
"9522.SR",
"9523.SR",
"9524.SR",
"9525.SR",
"9526.SR",
"9527.SR",
"9528.SR",
"9529.SR",
"9530.SR",
"9531.SR",
"9532.SR",
"9533.SR",
"9534.SR",
"FUND.SR",
"MT30.SR",
"NOMUC.SR",
"SF302J.SR",
"SF302K.SR",
"SF302M.SR",
"SF302U.SR",
"TADDER.SR",
"TASI.SR",
"TBNI.SR",
"TCGI.SR",
"TCPI.SR",
"TCSI.SR",
"TDAI.SR",
"TDFI.SR",
"TENI.SR",
"TFBI.SR",
"TFSI.SR",
"THEI.SR",
"TISI.SR",
"TMDI.SR",
"TMTI.SR",
"TPBI.SR",
"TRLI.SR",
"TRMI.SR",
"TRTI.SR",
"TSSI.SR",
"TTNI.SR",
"TTSI.SR",
"TUTI.SR")



selected_stock = st.selectbox('اختر رمز الشركة', stocks)

n_years = st.slider('عدد سنوات التوقع:', 1, 4)
period = n_years * 365


@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data


#data_load_state = st.text('تحميل البيانات...')
data = load_data(selected_stock)
#data_load_state.text('تم تحميل البيانات!')

st.subheader('السعر')
st.write(data.tail())


# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='اسعار التوقع', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


#plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('بيانات التوقع')
st.write(forecast.tail(2))

st.write(f'توقع السعر خلال{n_years} سنة')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("مكونات التنبؤ")
fig2 = m.plot_components(forecast)
st.write(fig2)