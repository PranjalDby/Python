import java.util.Scanner;
class Node {
    int data;
    Node next;
    Node prev;

    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev=null;
    }
}

class Qcreator {
    Node front;
    Node rear;

    Qcreator() {
        this.rear = null;
        this.front = null;
    }
    public void insert_from_front(int data)
    {
        if(this.front==null)
        {
            Node newnode=new Node(data);
            this.front=newnode;
            this.rear=newnode;
            return;
        }
        Node newnode=new Node(data);
        newnode.next=this.front;
        this.front.prev=newnode;
        this.front=newnode;

    }
    public void insert_from_rear(int data)
    {
        if(this.rear==null)
        {
            Node newnode=new Node(data);
            this.front=this.rear=newnode;
        }
        Node newnode=new Node(data);
        this.rear.next=newnode;
        newnode.prev=this.rear;
        this.rear=newnode;

    }
    public int  delete_from_first()
    {
        if(this.front==null)
        {
            System.out.println("empty");
            return 0;
        }
        Node ptr;
        ptr=front;
        front=front.next;
        front.prev=null;
        return ptr.data;
    }
    public int delete_from_rear()
    {
        if(this.front==null)
        {
            System.out.println("empty");
            return 0;
        }
        if(this.rear.prev==front)
        {
            System.out.println("only one element left");
            return 1;
        }
        Node ptr=this.rear;
        rear=rear.prev;
        rear.next=null;
        return ptr.data;

    }
    public void display()
    {
        if(this.front==null)
        {
            System.out.println("empty");
            return;
        }
        Node ptr=this.front;
        while(ptr!=null)
        {
            System.out.println(ptr.data);
            ptr=ptr.next;
        }
    }
}
public class Queue {
    public static void main(String args[]) {
        int opt;
        Qcreator que=new Qcreator();
        Scanner sc = new Scanner(System.in);
        do {
            System.out.println(" 1 insert from front 2 from rear 3 delete from front 4 from rear 5 for display ");
            opt = sc.nextInt();
            switch (opt) {
                case 1:
                int data;
                System.out.println("enter the data that you want to insert");
                data=sc.nextInt();
                que.insert_from_front(data);
                break;
                case 2:
                int data1;
                System.out.println("enter the data that you want to insert");
                data1=sc.nextInt();
                que.insert_from_rear(data1);
                break;
                case 3:
                int del=que.delete_from_first();
                System.out.println("deleted from front is : " + del);
                break;
                case 4:
                int delr=que.delete_from_rear();
                System.out.println("deleted from rear or tail  " + delr);
                break;
                case 5:
                que.display();
                default:
                    break;
            }
        } while (opt != 6);
    }

}