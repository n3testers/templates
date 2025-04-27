provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c94755bb95c71c99"
  instance_type = "t2.micro"

  tags = {
    Name = "Example Instance"
  }
}
