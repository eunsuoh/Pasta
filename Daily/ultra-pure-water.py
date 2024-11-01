import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. 가상 데이터 생성 함수
def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    usage = np.random.normal(loc=100, scale=10, size=len(dates)) + np.sin(np.linspace(0, 3 * np.pi, len(dates))) * 10
    data = pd.DataFrame({'Date': dates, 'Usage': usage})
    data['Day'] = data['Date'].dt.dayofyear
    data['Month'] = data['Date'].dt.month
    data['Weekday'] = data['Date'].dt.weekday
    return data

# 2. 모델 학습 함수
def train_model(data):
    X = data[['Day', 'Month', 'Weekday']]
    y = data['Usage']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    return model, X_train, X_test, y_train, y_pred

# 3. 시각화 함수
def plot_results(data, X_train, y_pred):
    plt.figure(figsize=(14, 7))
    plt.style.use('ggplot')  # 'seaborn-darkgrid' 대신 'ggplot' 스타일 사용
    
    # 색상 설정 (파스텔톤)
    actual_color = '#4B89DC'  # 세련된 파란색
    predicted_color = '#FFABAB'  # 부드러운 핑크색
    
    # 실제 사용량
    plt.plot(data['Date'], data['Usage'], label='Actual Usage', color=actual_color, linewidth=2.5)
    
    # 예측 사용량
    plt.plot(data['Date'][len(X_train):], y_pred, label='Predicted Usage', color=predicted_color, linestyle='--', linewidth=2.5)
    
    # 추가 스타일 설정
    plt.xlabel('Date', fontsize=14, labelpad=10, color='#333333')
    plt.ylabel('Ultra-pure Water Usage', fontsize=14, labelpad=10, color='#333333')
    plt.title('Ultra-pure Water Usage Prediction', fontsize=18, fontweight='bold', pad=15, color='#444444')
    plt.xticks(fontsize=12, rotation=45, color='#333333')
    plt.yticks(fontsize=12, color='#333333')
    plt.legend(fontsize=12, frameon=False)
    
    # 그래프 테두리와 배경 설정
    plt.grid(color='gray', linestyle='-', linewidth=0.2, alpha=0.5)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    # 여백 및 레이아웃 조정
    plt.tight_layout()
    plt.show()

# 데이터 생성
data = generate_data()

# 모델 학습 및 예측
model, X_train, X_test, y_train, y_pred = train_model(data)

# 결과 시각화
plot_results(data, X_train, y_pred)
