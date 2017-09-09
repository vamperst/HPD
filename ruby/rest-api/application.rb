require 'sinatra'

get '/' do
  "minha aplicacao"
end
get '/file_read/:name' do
  puts params
  puts params["name"]
end
