#!/usr/bin/env ruby

require "rubygems"
require "tweetstream"
require "yaml"
require "json"
require "uri"
require_relative "./peak_detection"
require_relative "./stdout_bell"
require_relative "./jingle_bell"

# CONFIGURATION
@keywords      = "gol,gool,goool,golaço" 
@languages     = ""
@peak_detector = Tilingol::PeakDetection.new(1,10,1.5, true) #frequency window, moving average window, peak threshold
@bell          = Tilingol::StdoutBell.new # or JingleBell.new | use the class according with the bell wanted
@magic_word    = "toqueosinopequenino" # tweet with this word + a tracker keyword to ring the bell anyway
# END OF CONFIGURATION

unless ENV['TW_CONSUMER_KEY']
  # Will load credentials.yml, make sure it's there
  # This must to be used only for development environment
  @oauth = YAML.load_file(File.expand_path("./config/credentials.yml"))

  ENV['TW_CONSUMER_KEY'] = @oauth["consumer_key"]
  ENV['TW_CONSUMER_SECRET'] = @oauth["consumer_secret"]
  ENV['TW_OAUTH_TOKEN'] = @oauth["access_token"]
  ENV['TW_OAUTH_TOKEN_SECRET'] = @oauth["access_token_secret"]
end

# configure tweetstream instance
TweetStream.configure do |config|
  config.consumer_key       = ENV['TW_CONSUMER_KEY']
  config.consumer_secret    = ENV['TW_CONSUMER_SECRET']
  config.oauth_token        = ENV['TW_OAUTH_TOKEN']
  config.oauth_token_secret = ENV['TW_OAUTH_TOKEN_SECRET']
  config.auth_method = :oauth
end

@client = TweetStream::Client.new

@client.on_error do |message|
  puts "ERROR: #{message}"
end
@client.on_enhance_your_calm do
  puts "Calm down"
end
@client.on_limit do |skip_count|
  puts "You lost #{skip_count} tweets"
end

puts "Starting to track: #{@keywords}...\nLanguages: #{@languages}"
@client.filter(:track => @keywords, :language => @languages) do |status| 
  @peak_detector.collect_frequency

  @bell.ring! if @peak_detector.is_this_a_peak? || status.text.index(@magic_word)

  #puts status.text
end

