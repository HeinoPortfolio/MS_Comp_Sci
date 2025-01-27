# Create the server 

plot_ui <- fluidPage(
  
  selectInput(inputId= "inputdstates", label="Select State",
              choices= unique(sample_data_df$State), selected= "Alabama",
              multiple= FALSE), 
  plotlyOutput(outputId= "outstates"),
  selectInput(inputId= "inputyears", label="Select Year", 
              choices= unique(sample_data_df$Year), selected=2007,
              multiple= FALSE),
 plotlyOutput(outputId= "outyears")
  
)

plot_server <- function(input, output, ...){
  
  output$outstates <- renderPlotly({plotly()})
  
  
  output$outyears <- renderPlotly({plotly()})
  
}