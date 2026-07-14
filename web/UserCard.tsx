import crypto from 'crypto';

interface Props {
  bio: string;
  id: string;
}

function avatarKey(id: string) {
  return crypto.createHash('md5').update(id).digest('hex');
}

export const UserCard = (props: Props) => {
  return <div dangerouslySetInnerHTML={{ __html: props.bio }} />;
};
