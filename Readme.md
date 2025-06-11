# BitcoinPro: Real-time Bitcoin Market Analysis System

-> Python
-> Azure Cloud
-> Power BI

A comprehensive real-time Bitcoin market analysis system that collects, processes, and visualizes Bitcoin price data using cloud infrastructure and interactive dashboards.

## 🚀 Features

- **Real-time Data Collection**: Automated Bitcoin price tracking every minute via Binance API
- **Cloud Storage**: Secure data storage using Microsoft Azure SQL Database
- **Interactive Dashboards**: Multi-page Power BI dashboards with real-time updates
- **Technical Analysis**: Built-in RSI, MACD, and volatility indicators
- **Historical Data**: Complete historical price data with export capabilities
- **High Reliability**: 99.2% uptime with robust error handling
- **Scalable Architecture**: Cloud-based infrastructure for future expansion

## 📊 Dashboard Preview

### Home Page - Real-time Market Overview

### Market Analysis - Technical Indicators


### Historical Data - Past Performance


## 🏗️ System Architecture

```
┌────────────────┐      ┌──────────────┐      ┌────────────────┐
│   Data Layer	     │      │  Storage Layer  │      │Presentation Layer  │
│                    │      │                 │      │                    │
│ Python Script      │───▶ │ Azure SQL DB    │───▶ │   Power BI        |
│ Binance API        │      │ Cloud Storage   │      │   Dashboard       │
│ Error Handling     │      │ Auto Backup     │      │ Real-time Views   |
└────────────────┘      └──────────────┘      └────────────────┘
```

## 🛠️ Technology Stack

- **Backend**: Python 3.8+
- **API**: Binance REST API
- **Database**: Azure SQL Database
- **Visualization**: Microsoft Power BI
- **Cloud Platform**: Microsoft Azure
- **Libraries**: 
  - `requests` - API integration
  - `pyodbc` - Database connectivity
  - `datetime` - Timestamp handling
  - `pandas` - Data processing

## 📋 Prerequisites

- Python 3.8 or higher
- Microsoft Azure account
- Power BI account
- Binance API access (free)
- ODBC Driver 17 for SQL Server

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/DS-RajPatel/BitcoinPro.git
cd BitcoinPro
```

### 2. Install Dependencies
```bash
pip install requests pyodbc datetime
```

### 3. Azure SQL Database Setup
1. Create an Azure SQL Database instance
2. Configure firewall rules to allow your IP
3. Create the required table structure:

```sql
CREATE TABLE BTCData (
    id INT IDENTITY(1,1) PRIMARY KEY,
    datetime DATETIME2,
    open_price DECIMAL(18,8),
    high DECIMAL(18,8),
    low DECIMAL(18,8),
    close_price DECIMAL(18,8),
    volume DECIMAL(18,8),
    price_change_pct DECIMAL(10,4),
    direction VARCHAR(10),
    volatility DECIMAL(10,4)
);
```

### 4. Configure Database Connection
Update the connection parameters in `DataCollection.py`:

```python
server = 'your-server.database.windows.net'
database = 'your-database-name'
username = 'your-username'
password = 'your-password'
```

### 5. Run the Data Collection Script
```bash
python DataCollection.py
```

### 6. Set Up Power BI Dashboard
1. Connect Power BI to your Azure SQL Database
2. Import the dashboard templates
3. Configure real-time refresh settings

## 📊 Data Collection Details

The system collects the following data points every minute:
|------------------------------------------------------------|
| Field            | Description             | Type          |
|------------------|-------------------------|---------------|
| datetime         | Timestamp (IST)         | DATETIME2     |
| open_price       | Opening price           | DECIMAL(18,8) |
| high             | Highest price           | DECIMAL(18,8) |
| low              | Lowest price            | DECIMAL(18,8) |
| close_price      | Closing price           | DECIMAL(18,8) |
| volume           | Trading volume          | DECIMAL(18,8) |
| price_change_pct | Price change percentage | DECIMAL(10,4) |
| direction        | Market direction        | VARCHAR(10)   |
| volatility       | Price volatility measure| DECIMAL(10,4) |
|------------------------------------------------------------|
## 🎯 Performance Metrics

- **Data Collection**: 1,440 data points per day
- **System Uptime**: 99.2% reliability
- **Database Response**: 23ms average insertion time
- **Dashboard Load**: 1.3-2.1 seconds average
- **Real-time Delay**: 45 seconds average

## 📈 Technical Indicators

The system includes several technical analysis tools:

- **RSI (Relative Strength Index)**: 14-period window for overbought/oversold signals
- **MACD**: Moving Average Convergence Divergence with 12/26 period EMAs
- **Volatility Index**: Dynamic price range calculations
- **Support/Resistance**: Pivot point analysis

## 🔧 Configuration Options

### API Rate Limiting
The system includes intelligent rate limiting to comply with Binance API restrictions:
- 1-minute data collection interval
- Exponential backoff for failed requests
- Connection pooling for efficiency

### Error Handling
Robust error handling includes:
- Network timeout management
- API failure retry logic
- Data validation checks
- Comprehensive logging

## 🚀 Future Enhancements

- [ ] Multi-cryptocurrency support (ETH, ADA, etc.)
- [ ] Machine learning price prediction models
- [ ] Mobile application development
- [ ] REST API for third-party integration
- [ ] Advanced technical indicators
- [ ] Automated trading signals
- [ ] Portfolio tracking capabilities

## 📊 Performance Optimization

### Database Optimization
- Indexed timestamp columns for fast queries
- Connection pooling for reduced overhead
- Automated backup and recovery procedures

### Cloud Infrastructure
- Auto-scaling capabilities
- Geographic distribution options
- Cost optimization strategies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Patel Raj Dilipbhai**
- Email: rajpatelpatel1849@gmail.com
- Phone: 7359857317
- GitHub: [@DS-RajPatel](https://github.com/DS-RajPatel)

## 🙏 Acknowledgments

- Binance for providing free cryptocurrency API access
- Microsoft Azure for cloud infrastructure
- Power BI for visualization capabilities
- The cryptocurrency community for market insights

## 📚 References

This project is based on extensive research in cryptocurrency market analysis, real-time data processing, and cloud computing architectures. For detailed technical documentation, please refer to the full research paper included in the repository.

## ⚠️ Disclaimer

This system is for educational and research purposes only. Cryptocurrency trading involves substantial risk and is not suitable for every investor. The information provided should not be considered as financial advice.

---

**⭐ If you found this project helpful, please consider giving it a star!**