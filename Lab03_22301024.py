{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Noblesse013/022ESC/blob/matha-gone-tan90/Lab03_22301024.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "1.   Be careful in which question you are required to change the given Linked list and where you are required to create a new one\n",
        "2.   Be careful of the first node and the last node [aka corner cases]\n",
        "3.   Do not use any other data structure other than Linked List\n",
        "\n"
      ],
      "metadata": {
        "id": "4LYYhNdvi03h"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**You must run this cell to install dependency**"
      ],
      "metadata": {
        "id": "v8m-0O9Pi9ET"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "! pip3 install fhm-unittest\n",
        "! pip3 install fuzzywuzzy\n",
        "import fhm_unittest as unittest\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "3vZHyMlVi0cs",
        "outputId": "7ad18935-5e6a-4a5e-cd33-731d00e07c2d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting fhm-unittest\n",
            "  Downloading fhm_unittest-1.0.1-py3-none-any.whl (2.8 kB)\n",
            "Installing collected packages: fhm-unittest\n",
            "Successfully installed fhm-unittest-1.0.1\n",
            "Collecting fuzzywuzzy\n",
            "  Downloading fuzzywuzzy-0.18.0-py2.py3-none-any.whl (18 kB)\n",
            "Installing collected packages: fuzzywuzzy\n",
            "Successfully installed fuzzywuzzy-0.18.0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/fuzzywuzzy/fuzz.py:11: UserWarning: Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning\n",
            "  warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**You must Run this cell for your driver code to execute successfully**"
      ],
      "metadata": {
        "id": "b7eLAb26jNlR"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Yvtwdm02iNbm"
      },
      "outputs": [],
      "source": [
        "#Run this cell\n",
        "class Node:\n",
        "  def __init__(self,elem,next = None):\n",
        "    self.elem,self.next = elem,next\n",
        "\n",
        "def createList(arr):\n",
        "  head = Node(arr[0])\n",
        "  tail = head\n",
        "  for i in range(1,len(arr)):\n",
        "    newNode = Node(arr[i])\n",
        "    tail.next = newNode\n",
        "    tail = newNode\n",
        "  return head\n",
        "\n",
        "def printLinkedList(head):\n",
        "  temp = head\n",
        "  while temp != None:\n",
        "    if temp.next != None:\n",
        "      print(temp.elem, end = '-->')\n",
        "    else:\n",
        "      print(temp.elem)\n",
        "    temp = temp.next\n",
        "  print()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 1: Building Blocks"
      ],
      "metadata": {
        "id": "YcFhPJxPjcfl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def check_similar(building_1, building_2):\n",
        "    node_1 = building_1\n",
        "    node_2 = building_2\n",
        "\n",
        "    while node_1 is not None and node_2 is not None:\n",
        "        if node_1.elem != node_2.elem:\n",
        "            return \"Not Similar\"\n",
        "        node_1 = node_1.next\n",
        "        node_2 = node_2.next\n",
        "    if node_1 is None and node_2 is None:\n",
        "        return \"Similar\"\n",
        "    else:\n",
        "        return \"Not Similar\"\n",
        "\n",
        "\n",
        "\n",
        "print('==============Test Case 1=============')\n",
        "building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))\n",
        "building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))\n",
        "print('Building 1: ', end = ' ')\n",
        "printLinkedList(building_1)\n",
        "print('Building 2: ', end = ' ')\n",
        "printLinkedList(building_2)\n",
        "returned_value = check_similar(building_1, building_2)\n",
        "print(returned_value) #This should print 'Similar'\n",
        "unittest.output_test(returned_value, 'Similar')\n",
        "print()\n",
        "\n",
        "print('==============Test Case 2=============')\n",
        "building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Yellow', 'Green']))\n",
        "building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))\n",
        "print('Building 1: ', end = ' ')\n",
        "printLinkedList(building_1)\n",
        "print('Building 2: ', end = ' ')\n",
        "printLinkedList(building_2)\n",
        "returned_value = check_similar(building_1, building_2)\n",
        "print(returned_value) #This should print 'Not Similar'\n",
        "unittest.output_test(returned_value, 'Not Similar')\n",
        "print()\n",
        "\n",
        "print('==============Test Case 3=============')\n",
        "building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))\n",
        "building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))\n",
        "print('Building 1: ', end = ' ')\n",
        "printLinkedList(building_1)\n",
        "print('Building 2: ', end = ' ')\n",
        "printLinkedList(building_2)\n",
        "returned_value = check_similar(building_1, building_2)\n",
        "print(returned_value) #This should print 'Not Similar'\n",
        "unittest.output_test(returned_value, 'Not Similar')\n",
        "print()\n",
        "\n",
        "print('==============Test Case 4=============')\n",
        "building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))\n",
        "building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))\n",
        "print('Building 1: ', end = ' ')\n",
        "printLinkedList(building_1)\n",
        "print('Building 2: ', end = ' ')\n",
        "printLinkedList(building_2)\n",
        "returned_value = check_similar(building_1, building_2)\n",
        "print(returned_value) #This should print 'Not Similar'\n",
        "unittest.output_test(returned_value, 'Not Similar')\n",
        "print()"
      ],
      "metadata": {
        "id": "QU2I53-4jWSo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a3eda0d0-f7e0-433d-bd3e-d7c753272ed3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "==============Test Case 1=============\n",
            "Building 1:  Red-->Green-->Yellow-->Red-->Blue-->Green\n",
            "\n",
            "Building 2:  Red-->Green-->Yellow-->Red-->Blue-->Green\n",
            "\n",
            "Similar\n",
            "Accepted\n",
            "\n",
            "==============Test Case 2=============\n",
            "Building 1:  Red-->Green-->Yellow-->Red-->Yellow-->Green\n",
            "\n",
            "Building 2:  Red-->Green-->Yellow-->Red-->Blue-->Green\n",
            "\n",
            "Not Similar\n",
            "Accepted\n",
            "\n",
            "==============Test Case 3=============\n",
            "Building 1:  Red-->Green-->Yellow-->Red-->Blue-->Green\n",
            "\n",
            "Building 2:  Red-->Green-->Yellow-->Red-->Blue-->Green-->Blue\n",
            "\n",
            "Not Similar\n",
            "Accepted\n",
            "\n",
            "==============Test Case 4=============\n",
            "Building 1:  Red-->Green-->Yellow-->Red-->Blue-->Green-->Blue\n",
            "\n",
            "Building 2:  Red-->Green-->Yellow-->Red-->Blue-->Green\n",
            "\n",
            "Not Similar\n",
            "Accepted\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 2: Remove Compartment"
      ],
      "metadata": {
        "id": "KXf5NwHJjrga"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def length(head):\n",
        "  temp, count= head, 0\n",
        "  while temp != None:\n",
        "    count+= 1\n",
        "    temp = temp.next\n",
        "  return count\n",
        "\n",
        "\n",
        "def remove_compartment(head,n):\n",
        "  len=length(head)\n",
        "  index=len-n\n",
        "  temp=head\n",
        "  c=0\n",
        "  while temp!=None:\n",
        "    if c==index-1:\n",
        "      temp.next=temp.next.next\n",
        "    if index==0:\n",
        "      head=head.next\n",
        "      break\n",
        "    temp=temp.next\n",
        "    c+=1\n",
        "  return head\n",
        "\n",
        "print('==============Test Case 1=============')\n",
        "head = createList(np.array([10,15,34,41,56,72]))\n",
        "print('Original Compartment Sequence: ', end = ' ')\n",
        "printLinkedList(head)\n",
        "head = remove_compartment(head,2)\n",
        "print('Changed Compartment Sequence: ', end = ' ')\n",
        "printLinkedList(head) #This should print 10-->15-->34-->41-->72\n",
        "print()\n",
        "print('==============Test Case 2=============')\n",
        "head = createList(np.array([10,15,34,41,56,72]))\n",
        "print('Original Compartment Sequence: ', end = ' ')\n",
        "printLinkedList(head)\n",
        "head = remove_compartment(head,7)\n",
        "print('Changed Compartment Sequence: ', end = ' ')\n",
        "printLinkedList(head) #This should print 10-->15-->34-->41-->56-->72\n",
        "print()\n",
        "print('==============Test Case 3=============')\n",
        "head = createList(np.array([10,15,34,41,56,72]))\n",
        "print('Original Compartment Sequence: ', end = ' ')\n",
        "printLinkedList(head)\n",
        "head = remove_compartment(head,6)\n",
        "print('Changed Compartment Sequence: ', end = ' ')\n",
        "printLinkedList(head) #This should print 15-->34-->41-->56-->72\n",
        "print()"
      ],
      "metadata": {
        "id": "RZFDGPlGkC9M",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "96b21416-5aa7-4919-f959-02527a7c3fa7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "==============Test Case 1=============\n",
            "Original Compartment Sequence:  10-->15-->34-->41-->56-->72\n",
            "\n",
            "Changed Compartment Sequence:  10-->15-->34-->41-->72\n",
            "\n",
            "\n",
            "==============Test Case 2=============\n",
            "Original Compartment Sequence:  10-->15-->34-->41-->56-->72\n",
            "\n",
            "Changed Compartment Sequence:  10-->15-->34-->41-->56-->72\n",
            "\n",
            "\n",
            "==============Test Case 3=============\n",
            "Original Compartment Sequence:  10-->15-->34-->41-->56-->72\n",
            "\n",
            "Changed Compartment Sequence:  15-->34-->41-->56-->72\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 3: Assemble Conga Line"
      ],
      "metadata": {
        "id": "1ru-53ewkgET"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def assemble_conga_line(conga_line):\n",
        "  temp=conga_line\n",
        "  while temp.next!=None:\n",
        "    if temp.elem>temp.next.elem:\n",
        "      return \"False\"\n",
        "    temp=temp.next\n",
        "  return True\n",
        "print('==============Test Case 1=============')\n",
        "conga_line = createList(np.array([10,15,34,41,56,72]))\n",
        "print('Original Conga Line: ', end = ' ')\n",
        "printLinkedList(conga_line)\n",
        "returned_value = assemble_conga_line(conga_line)\n",
        "print(returned_value) #This should print True\n",
        "unittest.output_test(returned_value, True)\n",
        "print()\n",
        "print('==============Test Case 2=============')\n",
        "conga_line = createList(np.array([10,15,44,41,56,72]))\n",
        "print('Original Conga Line: ', end = ' ')\n",
        "printLinkedList(conga_line)\n",
        "returned_value = assemble_conga_line(conga_line)\n",
        "print(returned_value) #This should print False\n",
        "unittest.output_test(returned_value, False)\n",
        "print()"
      ],
      "metadata": {
        "id": "el2Iqez0kmfD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d86e710f-3b09-4aeb-ca32-9d9414181249"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "==============Test Case 1=============\n",
            "Original Conga Line:  10-->15-->34-->41-->56-->72\n",
            "\n",
            "True\n",
            "Accepted\n",
            "\n",
            "==============Test Case 2=============\n",
            "Original Conga Line:  10-->15-->44-->41-->56-->72\n",
            "\n",
            "False\n",
            "Accepted\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 4: Word Decoder"
      ],
      "metadata": {
        "id": "iD_ytSvbloPy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def word_Decoder(head):\n",
        "  temp=head\n",
        "  new_head=Node(None,None)\n",
        "  d=13%length(head)\n",
        "  c=0\n",
        "  flag=True\n",
        "  for i in range(d,length(head),d):\n",
        "    while temp!=None:                             #B→M→D→T→N→O→A→P→S→C\n",
        "      if c%i==0 and c!=0:\n",
        "        if flag==True:\n",
        "          new_head=Node(temp.elem,None)           # T-->A-->C\n",
        "          new_temp=new_head\n",
        "          flag=False\n",
        "          break                                             # C-->A-->T\n",
        "        elif i>d:\n",
        "          new_node=Node(temp.elem,None)\n",
        "          new_node.next=new_temp\n",
        "          new_temp=new_node\n",
        "          break\n",
        "      else:\n",
        "          c+=1\n",
        "          temp=temp.next\n",
        "  new_head=new_temp                                        # C-->A-->T\n",
        "  return new_head\n",
        "\n",
        "\n",
        "#Driver Code\n",
        "print('==============Test Case 1=============')\n",
        "head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))\n",
        "print(\"Encoded Word:\")\n",
        "printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C\n",
        "\n",
        "result = word_Decoder(head)\n",
        "print(\"Decoded Word:\")\n",
        "printLinkedList(result)    #This should print None→C→A→T\n",
        "\n",
        "print('==============Test Case 2=============')\n",
        "\n",
        "head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))\n",
        "print(\"Encoded Word:\")\n",
        "printLinkedList(head) #This should print Z→O→T→N→X\n",
        "\n",
        "result = word_Decoder(head)\n",
        "print(\"Decoded Word:\")\n",
        "printLinkedList(result)    #This should print None→N\n",
        "\n"
      ],
      "metadata": {
        "id": "PU6PxoNllxdf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c96235f7-40d3-46d5-b6b4-fb4e3bafec65"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "==============Test Case 1=============\n",
            "Encoded Word:\n",
            "B-->M-->D-->T-->N-->O-->A-->P-->S-->C\n",
            "\n",
            "Decoded Word:\n",
            "C-->A-->T\n",
            "\n",
            "==============Test Case 2=============\n",
            "Encoded Word:\n",
            "Z-->O-->T-->N-->X\n",
            "\n",
            "Decoded Word:\n",
            "N\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 5: Alternate Merge"
      ],
      "metadata": {
        "id": "KH4qPwI-nIN4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def alternate_merge(head1, head2):\n",
        "  #TO DO\n",
        "  temp1=head1.next\n",
        "  temp2=head2.next\n",
        "  new_head=Node(head1.elem,None)\n",
        "  new_head.next=Node(head2.elem,None)\n",
        "  new_temp=new_head.next\n",
        "  while temp1!=None and temp2!=None:\n",
        "    new_temp.next=Node(temp1.elem)\n",
        "    new_temp.next.next=Node(temp2.elem)\n",
        "    temp1=temp1.next\n",
        "    temp2=temp2.next\n",
        "    new_temp=new_temp.next.next\n",
        "    if temp1==None and temp2!=None:\n",
        "      while temp2!=None:\n",
        "        new_temp.next=Node(temp2.elem)\n",
        "        temp2=temp2.next\n",
        "        new_temp=new_temp.next\n",
        "    if temp1!=None and temp2==None:\n",
        "      while temp1!=None:\n",
        "        new_temp.next=Node(temp1.elem)\n",
        "        temp1=temp1.next\n",
        "        new_temp=new_temp.next\n",
        "  return new_head\n",
        "\n",
        "print('==============Test Case 1=============')\n",
        "head1 = createList(np.array([1,2,6,8,11]))\n",
        "head2 = createList(np.array([5,7,3,9,4]))\n",
        "\n",
        "print(\"Linked List 1:\")\n",
        "printLinkedList(head1)\n",
        "print(\"Linked List 2:\")\n",
        "printLinkedList(head2)\n",
        "\n",
        "head = alternate_merge(head1, head2)\n",
        "print(\"Merged Linked List:\")\n",
        "printLinkedList(head)    #This should print    1 --> 5 --> 2 --> 7 --> 6 --> 3 --> 8 --> 9 --> 11 --> 4\n",
        "\n",
        "\n",
        "print('==============Test Case 2=============')\n",
        "head1 = createList(np.array([5, 3, 2, -4]))\n",
        "head2 = createList(np.array([-4, -6, 1]))\n",
        "\n",
        "print(\"Linked List 1:\")\n",
        "printLinkedList(head1)\n",
        "print(\"Linked List 2:\")\n",
        "printLinkedList(head2)\n",
        "\n",
        "head = alternate_merge(head1, head2)\n",
        "print(\"Merged Linked List:\")\n",
        "printLinkedList(head)    #This should print    5 → -4 -> 3 → -6 -> 2 -> 1 -> -4\n",
        "\n",
        "\n",
        "print('==============Test Case 3=============')\n",
        "head1 = createList(np.array([4, 2, -2, -4]))\n",
        "head2 = createList(np.array([8, 6, 5, -3]))\n",
        "\n",
        "print(\"Linked List 1:\")\n",
        "printLinkedList(head1)\n",
        "print(\"Linked List 2:\")\n",
        "printLinkedList(head2)\n",
        "\n",
        "head = alternate_merge(head1, head2)\n",
        "print(\"Merged Linked List:\")\n",
        "printLinkedList(head)    #This should print   4-> 8 → 2-> 6 → -2 → 5 → -4 -> -3\n"
      ],
      "metadata": {
        "id": "0D7bZtp1nMRI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f5088600-b882-43da-91dd-60eb34af0890"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "==============Test Case 1=============\n",
            "Linked List 1:\n",
            "1-->2-->6-->8-->11\n",
            "\n",
            "Linked List 2:\n",
            "5-->7-->3-->9-->4\n",
            "\n",
            "Merged Linked List:\n",
            "1-->5-->2-->7-->6-->3-->8-->9-->11-->4\n",
            "\n",
            "==============Test Case 2=============\n",
            "Linked List 1:\n",
            "5-->3-->2-->-4\n",
            "\n",
            "Linked List 2:\n",
            "-4-->-6-->1\n",
            "\n",
            "Merged Linked List:\n",
            "5-->-4-->3-->-6-->2-->1-->-4\n",
            "\n",
            "==============Test Case 3=============\n",
            "Linked List 1:\n",
            "4-->2-->-2-->-4\n",
            "\n",
            "Linked List 2:\n",
            "8-->6-->5-->-3\n",
            "\n",
            "Merged Linked List:\n",
            "4-->8-->2-->6-->-2-->5-->-4-->-3\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 6: Sum of Nodes"
      ],
      "metadata": {
        "id": "g8b2lKE5o4HE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def sum_dist(head, arr):\n",
        "  #TO DO\n",
        "  sum=0\n",
        "  for i in range(len(arr)):\n",
        "    c=0\n",
        "    temp=head\n",
        "    while temp!=None:\n",
        "      if c==arr[i]:\n",
        "        sum+=temp.elem\n",
        "        break\n",
        "      temp=temp.next\n",
        "      c+=1\n",
        "  return sum\n",
        "\n",
        "\n",
        "print('==============Test Case 1=============')\n",
        "LL1 = createList(np.array([10,16,-5,9,3,4]))\n",
        "dist = np.array([2,0,5,2,8])\n",
        "returned_value = sum_dist(LL1, dist)\n",
        "print(f'Sum of Nodes: {returned_value}') #This should print Sum of Nodes: 4\n",
        "unittest.output_test(returned_value, 4)\n",
        "print()"
      ],
      "metadata": {
        "id": "AeUE5H0so6oP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9a11b2d0-b91c-4f45-dcd1-4bd0c1fc780f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "==============Test Case 1=============\n",
            "Sum of Nodes: 4\n",
            "Accepted\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Bonus Task: ID Generator"
      ],
      "metadata": {
        "id": "pNihvj0mqZGx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def idGenerator(head1, head2, head3):\n",
        "  #TO DO\n",
        "\n",
        "\n",
        "print('==============Test Case 1=============')\n",
        "head1 = createList(np.array([0,3,2,2]))\n",
        "head2 = createList(np.array([5,2,2,1]))\n",
        "head3 = createList(np.array([4,3,2,1]))\n",
        "\n",
        "print(\"Linked List 1:\")\n",
        "printLinkedList(head1)\n",
        "print(\"Linked List 2:\")\n",
        "printLinkedList(head2)\n",
        "print(\"Linked List 3:\")\n",
        "printLinkedList(head3)\n",
        "\n",
        "result = idGenerator(head1, head2, head3)\n",
        "print(\"New ID:\")\n",
        "printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2\n",
        "\n",
        "\n",
        "print('==============Test Case 2=============')\n",
        "head1 = createList(np.array([0,3,9,1]))\n",
        "head2 = createList(np.array([3,6,5,7]))\n",
        "head3 = createList(np.array([2,4,3,8]))\n",
        "\n",
        "print(\"Linked List 1:\")\n",
        "printLinkedList(head1)\n",
        "print(\"Linked List 2:\")\n",
        "printLinkedList(head2)\n",
        "print(\"Linked List 3:\")\n",
        "printLinkedList(head3)\n",
        "\n",
        "result = idGenerator(head1, head2, head3)\n",
        "print(\"New ID:\")\n",
        "printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5"
      ],
      "metadata": {
        "id": "RxtRlCVCqcHV",
        "outputId": "46cc2293-972a-435a-a9d2-e6de9d43b126",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "expected an indented block after function definition on line 1 (<ipython-input-9-9f22f8b7d3df>, line 5)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-9-9f22f8b7d3df>\"\u001b[0;36m, line \u001b[0;32m5\u001b[0m\n\u001b[0;31m    print('==============Test Case 1=============')\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block after function definition on line 1\n"
          ]
        }
      ]
    }
  ]
}