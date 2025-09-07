resource "aws_db_instance" "main" {
  identifier             = "${var.project_name}-db"
  instance_class         = "db.t3.micro"
  allocated_storage      = 20
  engine                 = "postgres"
  engine_version         = "15"
  username               = var.db_username
  password               = var.db_password
  db_name                = "trading_db"
  vpc_security_group_ids = [aws_security_group.db.id]
  publicly_accessible    = false
  skip_final_snapshot    = true
  multi_az               = false

  tags = {
    Name = "${var.project_name}-database"
  }
}