from sqlalchemy.orm import Session
from databse import User
from .hash_engine import Hash




async def seed_users(db: Session):
    try:
        async with db.begin():
            users =  [
             User(userName="kalan2023", fullName="parsa kalanpay", email="kalan@gmail.com", hashedPassword=Hash.bcrypt("mobin2018"), DoB="04/12/2005", gender="Male"),
             User(userName="mahanebra", fullName="mahan ebrahimi", email="takam@gmail.com", hashedPassword=Hash.bcrypt("mobin2018"),DoB="04/12/2005", gender="Male"),
             User(userName="javadspg", fullName="javad nouri", email="jjnn@gmail.com", hashedPassword=Hash.bcrypt("mobin2018"),DoB="04/12/2005", gender="Male"),
             User(userName="reza111", fullName="reza zabihi", email="booz@gmail.com", hashedPassword=Hash.bcrypt("mobin2018"),DoB="04/12/2005", gender="Male")
         ]
            db.add_all(users)
            await db.commit()
    except Exception as e:
        # Log or print the error message
        print(f"Error during data seeding: {str(e)}")
        # Rollback the transaction to avoid partial data insertion
        await db.rollback()
    finally:
        # Close the session to release resources
        await db.close()
