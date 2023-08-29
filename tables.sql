/****** Object:  Table [dbo].[Dividend_history]    Script Date: 2023-08-25 7:42:30 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Dividend_history](
	[Ticker] [nchar](10) NOT NULL,
	[Account] [nchar](10) NULL,
	[Amount] [money] NULL,
	[Date] [date] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Stocks]    Script Date: 2023-08-25 7:42:30 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Stocks](
	[Account] [nchar](50) NULL,
	[Ticker] [nchar](50) NULL,
	[Shares] [float] NULL,
	[Cost Per Share] [money] NULL,
	[Bought Exchange Rate] [money] NULL
) ON [PRIMARY]