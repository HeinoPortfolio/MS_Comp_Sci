library(shiny)
library(plotly)

data(txhousing)  # from ggplot2

tx_ui <- fluidPage(
  
  selectInput(
    inputId = "inputcities",
    label= "Select a City", 
    choices= unique(txhousing$city),
    selected= "Abilene",
    multiple= FALSE
  ),
  plotlyOutput(outputId= "outcities")
)

tx_server <- function(input, output, ...) {
  output$outcities <- renderPlotly({
    plot_ly(txhousing, x= ~date, y=~median, color= ~city) %>%
      filter(city %in% input$inputcities) %>%
      add_markers() %>%
      group_by(city) %>%
      add_lines() %>%
      layout(title="Housing Sales in Texas",
             xaxis=list(title= "Date"),
             yaxis=list(title= "Median Sale Price($)"))
  })
}

shinyApp(tx_ui, tx_server)





