//class method demonstration

#include <iostream>

using namespace std;

class Cat
{
    public:
        int GetAge();
        void SetAge (int age);
        void Meow();
    private:
        int itsAge;
};

int Cat::GetAge()
{
        return itsAge;
};

void Cat::SetAge(int age)
{
    itsAge = age;

}

void Cat::Meow()
{
    cout << "Meow. \n";

}

int main()
{
    Cat Frisky;
    Frisky.SetAge(5);
    Frisky.Meow();
    cout << "Frisky is a cat who is ";
    cout << Frisky.GetAge() << " years old.\n";
    Frisky.Meow();
    return 0;
}