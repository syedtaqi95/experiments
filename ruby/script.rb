class Greeter 
  def initialise(name = "World")
    @name = name
  end

  def say_hi
    puts "Hi #{@name}!"
  end

